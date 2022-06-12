from django.db import router
from rest_framework import routers
from interview.views.interview import InterviewViewSet
from interview.views.interview_report import InterviewReportViewSet
router = routers.DefaultRouter()
router.register(r'interviews', InterviewViewSet, 'interviews')
router.register(r'interviews', InterviewReportViewSet, 'interviews')