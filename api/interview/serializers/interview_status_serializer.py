from interview.models.interview_status import InterviewStatus
from rest_framework import serializers


class InterviewStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewStatus
        fields = '__all__'
