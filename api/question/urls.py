from django.db import router
from question.views.question_option import QuestionOptionViewSet
from question.views.question import QuestionViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet, 'questions')
router.register(r'question_options', QuestionOptionViewSet, 'question_options')