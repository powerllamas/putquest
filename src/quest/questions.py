# -*- coding: utf-8 -*-
from collections import namedtuple

from django import forms
from django.forms import widgets

QuestionData = namedtuple('QuestionData', 'label form')

class AnswerOpenForm(forms.Form):
    error_css_class = 'errors'
    required_css_class = 'required'

    text = forms.CharField(label=u"odpowiedź", widget=widgets.Textarea)

class AnswerSingleForm(forms.Form):
    error_css_class = 'errors'
    required_css_class = 'required'

    choices = [('a', 'aaa'), ('b', 'bbb')]
    choice = forms.ChoiceField(label=u"wybierz jedno", choices=choices, widget=widgets.RadioSelect)

class AnswerMultiForm(forms.Form):
    error_css_class = 'errors'
    required_css_class = 'required'

    choices = [('a', 'aaa'), ('b', 'bbb')]
    choice = forms.ChoiceField(label=u"zaznacz pasujące", choices=choices, widget=widgets.CheckboxSelectMultiple)

question_types = {
            'open': QuestionData('pytanie otwarte', AnswerOpenForm),
            'single_selection': QuestionData('pojedynczy wybór', AnswerSingleForm),
            'multi_selection': QuestionData('wielokrotny wybór', AnswerMultiForm),
        }

question_choices = []
for short, data in question_types.iteritems():
    choice = (short, data.label)
    question_choices.append(choice)

