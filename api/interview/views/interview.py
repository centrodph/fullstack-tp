from rest_framework import viewsets
from models.interview import Interview
from serializers.interview_serializer import InterviewSerializer


class InterviewViewSet(viewsets.ModelViewSet):
    """Event resource"""
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
