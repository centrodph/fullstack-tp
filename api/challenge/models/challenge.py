from django.conf import settings
from django.db import models

from question.models.question import Question

class Challenge(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=2000)
    update = models.DateField(auto_now=True)
    questions = models.ManyToManyField(Question, related_name='challenges')

    def __str__(self):
        return 'Question: '+self.title
