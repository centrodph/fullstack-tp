from django.db import router
from rest_framework import routers
from views.interview import InterviewViewSet

router = routers.DefaultRouter()
router.register(r'interviews', InterviewViewSet, 'interviews')