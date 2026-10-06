from rest_framework import serializers

from .models import Module, Progress, Question, Submission


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ("id", "name", "description", "level", "order")


class QuestionSerializer(serializers.ModelSerializer):
    module = ModuleSerializer(read_only=True)

    class Meta:
        model = Question
        fields = (
            "id",
            "module",
            "title",
            "description",
            "difficulty",
            "sample_input",
            "sample_output",
            "starter_code",
            "language_id",
            "time_limit",
            "memory_limit_kb",
        )


class SubmissionSerializer(serializers.ModelSerializer):
    question_title = serializers.CharField(source="question.title", read_only=True)

    class Meta:
        model = Submission
        fields = (
            "id",
            "question",
            "question_title",
            "code",
            "language_id",
            "status",
            "score",
            "execution_time",
            "memory_used",
            "judge_output",
            "error_output",
            "submitted_at",
            "judged_at",
        )
        read_only_fields = (
            "status",
            "score",
            "execution_time",
            "memory_used",
            "judge_output",
            "error_output",
            "submitted_at",
            "judged_at",
        )


class ProgressSerializer(serializers.ModelSerializer):
    module_name = serializers.CharField(source="module.name", read_only=True)

    class Meta:
        model = Progress
        fields = ("module_name", "attempted", "completed", "percentage", "updated_at")
