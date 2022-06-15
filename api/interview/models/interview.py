from django.conf import settings
from django.db import models

from candidate.models.candidate import Candidate
from challenge.models.challenge import Challenge
from interview.models.interview_status import InterviewStatus
class Interview(models.Model):
    description = description = models.TextField()
    interviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    candidate = models.ForeignKey(
        Candidate,
        related_name='candidates',
        on_delete=models.PROTECT,
        null=False,
    )
    challenge = models.ForeignKey(
        Challenge,
        related_name='challenges',
        on_delete=models.PROTECT,
        null=True,
    )
    status  = models.ForeignKey(
        InterviewStatus,
        related_name='interviewstatuses',
        on_delete=models.PROTECT,
        null=False,
    )
    code_access = models.CharField(max_length=2000, unique=True)
    date = models.DateTimeField()
    

    def __str__(self):
        return 'Interview: '+self.description
