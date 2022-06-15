from django.conf import settings
from django.db import models

class InterviewStatus(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return 'InterviewStatus: '+self.title
    class Meta:
        verbose_name_plural = "Interview statuses"