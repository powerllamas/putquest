# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from quest.questions import question_choices

class Questionnaire(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"nazwa")
    description = models.TextField(blank=True, verbose_name=u"opis")
    owner = models.ForeignKey(User, verbose_name=u"właściciel")
    public = models.BooleanField(verbose_name=u"publiczna")
    published = models.BooleanField(verbose_name=u"opublikowana")

    def __unicode__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"tytuł")
    text = models.TextField(verbose_name=u"treść pytania")
    questionnaire = models.ForeignKey(Questionnaire)
    number = models.IntegerField(verbose_name=u"kolejność")
    type = models.CharField(max_length=64, choices=question_choices, verbose_name=u"rodzaj pytania")

    def __unicode__(self):
        return self.title

class QuestionChoice(models.Model):
    question = models.ForeignKey(Question)
    name = models.CharField(max_length=200, verbose_name=u"treść wyboru")
    order = models.IntegerField(verbose_name=u"kolejność")

    def __unicode__(self):
        return self.name

class AnswerSet(models.Model):
    finished = models.BooleanField()

class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question)
    answer_set = models.ForeignKey(AnswerSet)
