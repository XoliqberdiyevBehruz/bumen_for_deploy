from rest_framework import serializers

from common.serializers import MediaURlSerializer
from supject.models import (
    Category,
    Step,
    StepFile,
    Subject,
    SubjectTitle,
    TestAnswer,
    TestQuestion,
    UserSubject,
)


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = [
            "id",
        ]


class SubjectSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ["id", "name", "type", "subject_title", "steps"]


class SubjectDetailSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)

    class Meta:
        model = Subject
        fields = ("id", "name", "type", "steps")


class UserSubjectSerializer(serializers.ModelSerializer):
    subject = SubjectDetailSerializer()

    class Meta:
        model = UserSubject
        fields = ["id", "subject", "total_test_ball", "started_time", "started"]


class SubjectTitleSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = SubjectTitle
        fields = ["id", "name", "category","subjects"]


class CategorySerializer(serializers.ModelSerializer):
    subject_titles = SubjectTitleSerializer(many=True, read_only=True, source='subjecttitle_set')

    class Meta:
        model = Category
        fields = ["id", "name", "click_count", "subject_titles"]


class SubjectTitleListSerializer(serializers.ModelSerializer):
    subjects = SubjectDetailSerializer(many=True)

    class Meta:
        model = SubjectTitle
        fields = ("id", "name", "subjects")


class StepFilesSerializer(serializers.ModelSerializer):
    file = MediaURlSerializer()

    class Meta:
        model = StepFile
        fields = ["id", "title", "file"]


class StepDetailSerializer(serializers.ModelSerializer):
    step_files = StepFilesSerializer(many=True)

    class Meta:
        model = Step
        fields = ["title", "description", "step_files"]


class StartStepTestSerializer(serializers.Serializer):
    step_id = serializers.IntegerField(required=True)


class TestAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAnswer
        fields = ("id", "answer")


class StepTestQuestionTestSerializer(serializers.ModelSerializer):
    test_answers = TestAnswerSerializer(many=True)

    class Meta:
        model = TestQuestion
        fields = ("id", "question_type", "question", "test_answers")
