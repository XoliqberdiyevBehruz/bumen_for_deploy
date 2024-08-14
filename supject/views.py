from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.models import User
import supject.serializers
from supject.models import *
from supject.serializers import *
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated


class CategoryAPIView(APIView):
    def get(self, request, pk):
        categories = Category.objects.all().order_by('-clicked_count')
        # orderby clicked_count buyicha
        categories_serializer = CategorySerializer(categories, many=True)
        content = {
            'categories': categories_serializer.data,
        }
        return Response(content, status=status.HTTP_200_OK)


class StartSubjectApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, subject_id):
        try:
            subject = Subject.objects.get(id=subject_id)
            serializer = SubjectSerializer(subject)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Subject.DoesNotExist:
            return Response({'error': 'Subject not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, subject_id):
        user = request.user
        try:
            subject = Subject.objects.get(id=subject_id)
        except Subject.DoesNotExist:
            return Response({"error": "Subject not found"}, status=status.HTTP_404_NOT_FOUND)
        # usersubject yaratamiz
        user_subject, created = UserSubject.objects.get_or_create(user=user, subject=subject)

        if created:
            user_subject.total_test_ball = 0.0
            user_subject.save()

        subject_serializers = SubjectSerializer(subject)
        return Response(subject_serializers.data, status=status.HTTP_200_OK)


class StartSubjectAPIView(ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]





