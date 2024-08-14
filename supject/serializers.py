from rest_framework import serializers
from supject.models import SubjectTitle, Category, Step, Subject, UserSubject


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id'
                  '', 'title', 'order', 'description']


class SubjectSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'name', 'type', 'subject_title', 'steps']


class UserSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubject
        fields = ['id', 'subject', 'user', 'total_test_ball']


class SubjectTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectTitle
        fields = ['name', 'category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'clicked_count']
