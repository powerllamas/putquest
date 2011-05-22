# -*- coding: utf-8 -*-
# quest/urls.py
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'quest.views.index', name='index'),
    url(r'^my_questionnaires$', 'quest.views.questionnaires_my', name='my_questionnaires'),

    url(r'^questionnaire/new/$', 'quest.views.questionnaire_modify',
        {
            'template': 'quest/questionnaire_new.html',
        },
        name='questionnaire_new'),

    url(r'^questionnaire/(?P<quest_id>\d+)/edit/$', 'quest.views.questionnaire_modify',
        {
            'template': 'quest/questionnaire_edit.html',
        }, name='questionnaire_edit'),

    url(r'^questionnaire/(?P<quest_id>\d+)/question/new/$', 
            'quest.views.question_modify',
            {
                'template': 'quest/question_new.html',
            }, name='question_new'),

    url(r'^questionnaire/(?P<quest_id>\d+)/question/(?P<question_id>\d+)/edit/$',
            'quest.views.question_modify',
            {
                'template': 'quest/question_edit.html',
            }, name='question_edit'),

    url(r'^questionnaire/(?P<quest_id>\d+)/$', 'quest.views.questionnaire', name='questionnaire'),
)
