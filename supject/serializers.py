from rest_framework import serializers

from supject.models import Category, Step, Subject, SubjectTitle, UserSubject


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step

        fields = ["id", "title", "order", "description"]


class SubjectSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ["id", "name", "type", "subject_title", "steps"]


class SubjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("id", "name", "type")


class UserSubjectSerializer(serializers.ModelSerializer):
    subject = SubjectDetailSerializer()

    class Meta:
        model = UserSubject
        fields = ["id", "subject", "total_test_ball", "started_time", "started"]


class SubjectTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectTitle
        fields = ["id", "name", "category"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "click_count"]


class SubjectTitleListSerializer(serializers.ModelSerializer):
    subjects = SubjectDetailSerializer(many=True)

    class Meta:
        model = SubjectTitle
        fields = ("id", "name", "subjects")
