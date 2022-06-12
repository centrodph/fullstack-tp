from rest_framework import viewsets
from question.models.question_option import QuestionOption
from question.serializers.question_option import QuestionOptionSerializer


class QuestionOptionViewSet(viewsets.ModelViewSet):
    """QuestionOption resource"""
    queryset = QuestionOption.objects.all()
    serializer_class = QuestionOptionSerializer
