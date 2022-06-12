from question.serializers.question import QuestionOptionSerializer
from challenge.models.challenge import Challenge
from rest_framework import serializers


class ChallengeSerializer(serializers.ModelSerializer):
    options=  QuestionOptionSerializer(many=True, read_only=True)
    class Meta:
        model = Challenge
        fields = '__all__'
