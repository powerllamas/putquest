# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from quest.questions import question_choices, question_types

class Questionnaire(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"nazwa")
    description = models.TextField(blank=True, verbose_name=u"opis")
    owner = models.ForeignKey(User, verbose_name=u"właściciel")
    public = models.BooleanField(verbose_name=u"publiczna")
    published = models.BooleanField(verbose_name=u"opublikowana")
    active = models.BooleanField(verbose_name=u"aktywna", default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"ankieta"
        verbose_name_plural = u"ankiety"

class Question(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"tytuł")
    text = models.TextField(verbose_name=u"treść pytania")
    questionnaire = models.ForeignKey(Questionnaire)
    number = models.IntegerField(verbose_name=u"kolejność")
    type = models.CharField(max_length=64, choices=question_choices, verbose_name=u"rodzaj pytania")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"pytanie"
        verbose_name_plural = u"pytania"

    def get_form_class(self):
        return question_types[self.type].form

class QuestionChoice(models.Model):
    question = models.ForeignKey(Question)
    name = models.CharField(max_length=200, verbose_name=u"treść wyboru")
    order = models.IntegerField(verbose_name=u"kolejność")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"wybór"
        verbose_name_plural = u"wybory"

class AnswerSet(models.Model):
    finished = models.BooleanField(verbose_name=u'zakończono')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name=u"wypełniająca/y")
    questionnaire = models.ForeignKey(Questionnaire)

    def __unicode__(self):
        return u"Ankieta '%s' wypełniona przez '%s'"

    class Meta:
        verbose_name = u"Wypełniona ankieta"
        verbose_name_plural = u"Wypełnione ankiety"


class Answer(models.Model):
    text = models.TextField()
    answer_set = models.ForeignKey(AnswerSet)
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return u"Odpowiedź na pytanie '%s'" % self.question

    class Meta:
        verbose_name = u"odpowiedź"
        verbose_name_plural = u"odpowiedzi"
