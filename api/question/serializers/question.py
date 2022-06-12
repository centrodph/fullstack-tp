from question.serializers.question_option import QuestionOptionSerializer
from question.models.question import Question
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    options=  QuestionOptionSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = '__all__'
