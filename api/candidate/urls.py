from django.db import router
from candidate.views.candidate import CandidateViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'candidates', CandidateViewSet, 'candidates')