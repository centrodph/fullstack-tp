from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from interview.models.interview_status import InterviewStatus
from interview.serializers.interview_status_serializer import InterviewStatusSerializer


class InterviewStatusViewSet(viewsets.ModelViewSet):
    """InterviewStatus resource"""
    queryset = InterviewStatus.objects.all()
    serializer_class = InterviewStatusSerializer