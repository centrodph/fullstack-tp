from django.conf import settings
from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    info_link = models.CharField(max_length=255)
    description = description = models.TextField()
    update = models.DateField(auto_now=True)

    def __str__(self):
        return 'Candidate: '+self.name
