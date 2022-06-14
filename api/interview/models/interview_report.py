from django.conf import settings
from django.db import models

from interview.models.interview import Interview
from candidate.models.candidate import Candidate
from challenge.models.challenge import Challenge
from question.models.question import Question
from question.models.question_option import QuestionOption

class InterviewReport(models.Model):
    interview = models.ForeignKey(
        Interview,
        related_name='interviews',
        on_delete=models.PROTECT,
        null=True,
    )
    candidate = models.ForeignKey(
        Candidate,
        # related_name='candidates',
        on_delete=models.PROTECT,
        null=True,
    )
    challenge = models.ForeignKey(
        Challenge,
        # related_name='challenges',
        on_delete=models.PROTECT,
        null=True,
    )
    question = models.ForeignKey(
        Question,
        related_name='questions',
        on_delete=models.PROTECT,
        null=True,
    )
    question_option = models.ForeignKey(
        QuestionOption,
        related_name='question_options',
        on_delete=models.PROTECT,
        null=True,
    )
    comments = models.TextField(max_length=500, null=True,)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Interview: '+str(self.interview.id)+' Candidate: '+self.candidate.name+' Challenge: '+self.challenge.title+' Question: '+self.question.title+' Option: '+str(self.question_option)
