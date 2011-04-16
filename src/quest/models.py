# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Questionnaire(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User)
    public = models.BooleanField()
    published = models.BooleanField()

    def __unicode__(self):
        return self.name

class Question(models.Model):
    text = models.TextField()
    questionnaire = models.ForeignKey(Questionnaire)

class AnswerSet(models.Model):
    finished = models.BooleanField()

class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question)
    answer_set = models.ForeignKey(AnswerSet)

