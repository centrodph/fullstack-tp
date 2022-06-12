from django.db import router
from challenge.views.challenge import ChallengeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'challenges', ChallengeViewSet, 'challenges')