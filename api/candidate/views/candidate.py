from rest_framework import viewsets
from candidate.models.candidate import Candidate
from candidate.serializers.candidate import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    """Candidate resource"""
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
