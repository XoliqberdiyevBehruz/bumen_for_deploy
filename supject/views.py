from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
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
