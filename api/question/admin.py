from django.contrib import admin
from question.models.question import Question
from question.models.question_option import QuestionOption

# Register your models here.
admin.site.register(Question)
admin.site.register(QuestionOption)