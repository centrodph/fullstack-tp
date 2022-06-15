from django.db import router
from rest_framework import routers
from interview.views.interview import InterviewViewSet
from interview.views.interview_report import InterviewReportViewSet
from interview.views.interview_status import InterviewStatusViewSet

router = routers.DefaultRouter()
router.register(r'interviews', InterviewViewSet, 'interviews')
router.register(r'interview_reports', InterviewReportViewSet, 'interview_reports')
router.register(r'interview_statuses', InterviewStatusViewSet, 'interview_statuses')