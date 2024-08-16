from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import supject.serializers
from account.models import User
from supject.models import *
from supject.serializers import *

category_id = openapi.Parameter(
    name="category_id", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER
)


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIView(APIView):
    def get(self, request, pk):
        categories = Category.objects.all().order_by("-click_count")
        # orderby clicked_count buyicha
        categories_serializer = CategorySerializer(categories, many=True)
        return Response(categories_serializer.data, status=status.HTTP_200_OK)


class SubjectListView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class StartSubjectApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, subject_id):
        user = request.user
        try:
            subject = Subject.objects.get(id=subject_id)
        except SubjectTitle.DoesNotExist:
            return Response(
                {"error": "Subject not found"}, status=status.HTTP_404_NOT_FOUND
            )
        # usersubject yaratamiz
        user_subject, created = UserSubject.objects.get_or_create(
            user=user, subject=subject
        )
        if created:
            user_subject.started = True
            user_subject.save()
        subject_serializer = UserSubjectSerializer(user_subject)
        return Response(data=subject_serializer.data, status=status.HTTP_200_OK)


class SubjectTitleApiView(ListAPIView):
    queryset = SubjectTitle.objects.all()
    serializer_class = SubjectTitleSerializer

    @swagger_auto_schema(manual_parameters=[category_id])
    def get(self, request, *args, **kwargs):
        query_param = request.query_params.get("category_id", None)
        if not query_param:
            return Response(data=[])
        subject_titles = SubjectTitle.objects.filter(category_id=query_param)
        serializer = SubjectTitleListSerializer(subject_titles, many=True)
        return Response(data=serializer.data)


class StepDetailAPIView(RetrieveAPIView):
    queryset = Step.objects.all().order_by("order")
    serializer_class = StepDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):

        try:
            step = self.get_object()
            user_subject = UserSubject.objects.filter(
                user=request.user, subject=step.subject, started=True
            )
            if user_subject.exists():
                if step.order == 1:
                    serailizer = self.serializer_class(step)
                    return Response(data=serailizer.data)
                next_step = Step.objects.get(order=step.order - 1)
                step_test = StepTest.objects.get(step=next_step)
                user_test_results = UserTotalTestResult.objects.filter(
                    step_test=step_test, user=request.user, ball__gte=60
                ).order_by("-ball")
                if user_test_results.exists():
                    serializer_new = self.serializer_class(next_step)
                    return Response(data=serializer_new.data)
                return Response(
                    data={"error": "You were not allowed to pass next step"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                return Response(
                    data={"error": "You didn't start subject yet"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Step.DoesNotExist:
            raise ValidationError("Step does not exists")
        except StepTest.DoesNotExist:
            raise ValidationError("Steptest does not exists")

        except Exception as e:
            raise APIException(e)


class StartStepTestView(CreateAPIView):
    queryset = StepTest.objects.all()
    serializer_class = StartStepTestSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            step = request.data.get("step_id")
            user_step = UserStep.objects.get(
                user=request.user, step=step, finished=False
            )
            step_test = StepTest.objects.get(step=step)
            if step_test.test_type == StepTest.TestTypes.MIDTERM:
                test_questions = TestQuestion.objects.filter(
                    Q(steptest=step_test)
                    & Q(
                        Q(level=TestQuestion.QuestionLevel.EASY)
                        | Q(level=TestQuestion.QuestionLevel.MEDIUM)
                    )
                ).order_by("?")[: step_test.question_count]
            else:
                test_questions = TestQuestion.objects.filter(
                    Q(steptest=step_test) & Q(Q(level=TestQuestion.QuestionLevel.HARD))
                ).order_by("?")[: step_test.question_count]
            user_test_result = UserTotalTestResult.objects.create(
                step_test=step_test,
                user=request.user,
            )
            user_step.finished = False
            user_step.save(update_fields=["finished"])
            data = {
                "result_id": user_test_result.id,
                "questions": StepTestQuestionTestSerializer(
                    test_questions, many=True
                ).data,
            }
            return Response(data=data)
        except Exception as e:
            raise APIException(e)
