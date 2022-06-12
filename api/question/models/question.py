from django.conf import settings
from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=120)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return 'Question: '+self.title
