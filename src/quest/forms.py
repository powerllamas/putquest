# -*- coding: utf-8 -*-
# quest/forms.py

from django import forms

from quest.models import Questionnaire

class QuestForm(forms.ModelForm):
    error_css_class = 'errors'
    required_css_class = 'required'

    class Meta:
        model = Questionnaire
        exclude = ['owner',]

class QuestionTypeForm(forms.Form):
    pass
