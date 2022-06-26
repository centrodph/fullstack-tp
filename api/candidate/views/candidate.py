from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from candidate.models.candidate import Candidate
from candidate.serializers.candidate import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    """Candidate resource"""
    permission_classes = [IsAuthenticated]
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
