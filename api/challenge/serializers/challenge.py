from question.serializers.question import QuestionSerializer
from challenge.models.challenge import Challenge
from rest_framework import serializers


class ChallengeSerializer(serializers.ModelSerializer):
    questions=  QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Challenge
        fields = '__all__'
