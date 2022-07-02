from rest_framework import viewsets
from interview.models.interview import Interview
from interview.serializers.interview_serializer import InterviewSerializer


class InterviewViewSet(viewsets.ModelViewSet):
    """Interview resource"""
    queryset = Interview.objects.all().order_by('-date')
    serializer_class = InterviewSerializer
