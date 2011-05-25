# -*- coding: utf-8 -*-
from django.contrib import admin
from quest.models import Questionnaire, Question, AnswerSet, Answer, QuestionChoice

class QuestionInline(admin.StackedInline):
    model = Question

class QuestionnaireAdmin(admin.ModelAdmin):
#    inlines = [
#        QuestionInline,
#    ]
    list_display = ['name', 'owner', 'public', 'published', 'active',]

# class AnswerInlineForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
        # super(AnswerInlineForm, self).__init__(*args, **kwargs)
        #self.fields['question'].queryset = Question.objects.filter(questionnaire=self.instance.answer_set.questionnaire)

class AnswerInline(admin.TabularInline):
    model = Answer
#   form = AnswerInlineForm

class AnswerSetAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline,
    ]

	
admin.site.register(AnswerSet, AnswerSetAdmin)	
admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Question)
admin.site.register(QuestionChoice)
admin.site.register(Answer)

