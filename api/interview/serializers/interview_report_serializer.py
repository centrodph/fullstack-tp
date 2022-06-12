# from candidate.serializers.candidate import CandidateSerializer
from interview.models.interview_report import InterviewReport
from rest_framework import serializers


class InterviewReportSerializer(serializers.ModelSerializer):
    # interviewer_username = serializers.CharField(source="interviewer.username", read_only=True)
    # candidate_data = CandidateSerializer(source="candidate", read_only=True)
    class Meta:
        model = InterviewReport
        fields = '__all__'
