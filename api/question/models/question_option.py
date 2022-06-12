from django.conf import settings
from django.db import models

from question.models.question import Question

class QuestionOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT, related_name='options')
    option = models.CharField(max_length=256)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return 'Option: '+self.option
