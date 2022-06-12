from rest_framework import viewsets
from challenge.models.challenge import Challenge
from challenge.serializers.challenge import ChallengeSerializer


class ChallengeViewSet(viewsets.ModelViewSet):
    """Candidate resource"""
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
