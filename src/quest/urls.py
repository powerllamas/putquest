# -*- coding: utf-8 -*-
# quest/urls.py
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'quest.views.index', name='index'),
    url(r'^questionnaire/(?P<quest_id>\d+)/', 'quest.views.questionnaire', name='questionnaire'),
)
