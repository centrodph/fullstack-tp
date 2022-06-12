from rest_framework import viewsets
from interview.models.interview_report import InterviewReport
from interview.serializers.interview_report_serializer import InterviewReportSerializer


class InterviewReportViewSet(viewsets.ModelViewSet):
    """InterviewReport resource"""
    queryset = InterviewReport.objects.all()
    serializer_class = InterviewReportSerializer
