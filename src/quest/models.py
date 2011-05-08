# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Questionnaire(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"nazwa")
    description = models.TextField(blank=True, verbose_name=u"opis")
    owner = models.ForeignKey(User, verbose_name=u"właściciel")
    public = models.BooleanField(verbose_name=u"publiczna")
    published = models.BooleanField(verbose_name=u"opublikowana")

    def __unicode__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    questionnaire = models.ForeignKey(Questionnaire)
    number = models.IntegerField()
    #class Meta:
    #    abstract = True

"""
class OpenQuestion(Question):
    pass

class SingleSelectionQuestion(Question):
    pass

class MultiSelectionQuestion(Question):
    pass

class NumberQuestion(Question):
    pass
"""

class AnswerSet(models.Model):
    finished = models.BooleanField()

class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question)
    answer_set = models.ForeignKey(AnswerSet)
    #class Meta:
    #    abstract = True

"""
class OpenAnswer(Answer):
    pass

class SingleSelectionAnswer(Answer):
    pass

class MultiSelectionAnswer(Answer):
    pass

class NumberAnswer(Answer):
    pass
"""
