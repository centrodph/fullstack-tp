from question.models.question_option import QuestionOption
from rest_framework import serializers


class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = '__all__'
