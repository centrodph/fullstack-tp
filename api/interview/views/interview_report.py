from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from interview.models.interview_report import InterviewReport
from interview.serializers.interview_report_serializer import InterviewReportSerializer


class InterviewReportViewSet(viewsets.ModelViewSet):
    """InterviewReport resource"""
    queryset = InterviewReport.objects.all()
    serializer_class = InterviewReportSerializer
    
    @action(detail=False, methods=['POST'])
    def save_question_answer(self, request):
        """Save question answer"""
        print(request.data)
        return Response({'status': status.HTTP_200_OK})