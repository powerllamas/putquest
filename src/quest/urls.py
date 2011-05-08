# -*- coding: utf-8 -*-
# quest/urls.py
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'quest.views.index', name='index'),
    url(r'^questionnaire/new/$', 'quest.views.questionnaire_new', name='questionnaire_new'),
    url(r'^questionnaire/edit/(?P<quest_id>\d+)/question/new/$', 
            'quest.views.question_new', name='question_new'),
    url(r'^questionnaire/edit/(?P<quest_id>\d+)/$', 'quest.views.questionnaire_edit', name='questionnaire_edit'),
    url(r'^questionnaire/edit/(?P<quest_id>\d+)/question/(?P<question_id>\d+)/$',
            'quest.views.question_edit', name='question_edit'),
    url(r'^questionnaire/(?P<quest_id>\d+)/$', 'quest.views.questionnaire', name='questionnaire'),
)
