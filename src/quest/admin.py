# -*- coding: utf-8 -*-
from django.contrib import admin
from quest.models import Questionnaire, Question, AnswerSet, Answer

admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(AnswerSet)
admin.site.register(Answer)
