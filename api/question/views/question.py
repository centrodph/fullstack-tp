from rest_framework import viewsets
from question.models.question import Question
from question.serializers.question import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """Candidate resource"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
