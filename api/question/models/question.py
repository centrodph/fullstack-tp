from django.conf import settings
from django.db import models

# from challenge.models.challenge import Challenge

class Question(models.Model):
    title = models.CharField(max_length=120)
    update = models.DateField(auto_now=True)
    # challenges = models.ManyToManyField(Challenge, related_name='questions')

    def __str__(self):
        return 'Question: '+self.title
