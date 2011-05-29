# -*- coding: utf-8 -*-
from collections import namedtuple

from django import forms
from django.forms import widgets

QuestionData = namedtuple('QuestionData', 'label form')

class AnswerBaseForm(forms.Form):
    def __init__(self, question, choice_field_name = 'choice', *args, **kwargs):
        if 'prefix' not in kwargs:
            kwargs['prefix'] = 'question_%s' % question.pk
        super(forms.Form, self).__init__(*args, **kwargs)
        if choice_field_name in self.fields:
            setattr(self.fields[choice_field_name], 'queryset', question.questionchoice_set.all())
        self._question = question

    error_css_class = 'errors'
    required_css_class = 'required'

class AnswerOpenForm(AnswerBaseForm):
    text = forms.CharField(label=u"odpowiedź", widget=widgets.Textarea)

    def save(self, answer_set):
        from quest.models import Answer
        text = self.cleaned_data['text']
        answer = Answer(text=text, answer_set=answer_set, question=self._question)
        answer.save()
        return answer

class AnswerSingleForm(AnswerBaseForm):
    choice = forms.ModelChoiceField(label=u"wybierz jedno", queryset=[], empty_label=None, widget=widgets.RadioSelect)

    def save(self, answer_set):
        from quest.models import Answer
        choices = [self.cleaned_data['choice'], ]
        answer = Answer(answer_set=answer_set, question=self._question)
        answer.save()
        answer.choices = choices
        return answer

class AnswerMultiForm(AnswerBaseForm):
    choice = forms.ModelMultipleChoiceField(label=u"zaznacz pasujące", queryset=[], widget=widgets.CheckboxSelectMultiple)

    def save(self, answer_set):
        from quest.models import Answer
        choices = self.cleaned_data['choice']
        answer = Answer(answer_set=answer_set, question=self._question)
        answer.save()
        answer.choices = choices
        return answer

question_types = {
            'open': QuestionData('pytanie otwarte', AnswerOpenForm),
            'single_selection': QuestionData('pojedynczy wybór', AnswerSingleForm),
            'multi_selection': QuestionData('wielokrotny wybór', AnswerMultiForm),
        }

question_choices = []
for short, data in question_types.iteritems():
    choice = (short, data.label)
    question_choices.append(choice)

