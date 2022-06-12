from interview.models.interview import Interview
from rest_framework import serializers


class InterviewSerializer(serializers.ModelSerializer):
    interviewer_username = serializers.CharField(source="interviewer.username", read_only=True)
    class Meta:
        model = Interview
        fields = '__all__'
