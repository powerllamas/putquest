# -*- coding: utf-8 -*-
# quest/forms.py

from django import forms

from quest.models import Questionnaire
from quest.questions import question_types

class QuestForm(forms.ModelForm):
    error_css_class = 'errors'
    required_css_class = 'required'

    class Meta:
        model = Questionnaire
        exclude = ['owner',]

class QuestionTypeForm(forms.Form):
    error_css_class = 'errors'
    required_css_class = 'required'

    choices = []
    for k,v in question_types.iteritems():
        choice = (k, v[0])
        choices.append(choice)
    question_type = forms.ChoiceField(label="Typ pytania", choices=choices)
