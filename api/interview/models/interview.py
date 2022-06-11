from django.conf import settings
from django.db import models

class Interview(models.Model):
    description = description = models.TextField()
    interviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    code_access = models.CharField(max_length=2000, unique=True)
    date = models.DateTimeField()

    def __str__(self):
        return 'Interview: '+self.description
