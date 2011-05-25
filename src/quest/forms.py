# -*- coding: utf-8 -*-
# quest/forms.py

from django import forms
from django.forms.models import inlineformset_factory
from django.forms import widgets

from quest.models import Questionnaire, Question, QuestionChoice
from quest.questions import question_choices

class QuestForm(forms.ModelForm):
    error_css_class = 'errors'
    required_css_class = 'required'

    class Meta:
        model = Questionnaire
        exclude = ['owner', 'active']

class QuestionTypeForm(forms.Form):
    error_css_class = 'errors'
    required_css_class = 'required'

    question_type = forms.ChoiceField(label="Typ pytania", choices=question_choices)

class QuestionForm(forms.ModelForm):
    error_css_class = 'errors'
    required_css_class = 'required'

    class Meta:
        model = Question
        exclude = ['questionnaire']

class QuestionChoiceForm(forms.ModelForm):
    error_css_class = 'errors'
    required_css_class = 'required'

    class Meta:
        model = QuestionChoice
        exclude = ['question']

ChoiceFormSet = inlineformset_factory(Question, QuestionChoice)
