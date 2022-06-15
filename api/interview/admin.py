from django.contrib import admin

from interview.models.interview_report import InterviewReport
from interview.models.interview import Interview
from interview.models.interview_status import InterviewStatus
# Register your models here.
admin.site.register(Interview)
admin.site.register(InterviewReport)
admin.site.register(InterviewStatus)