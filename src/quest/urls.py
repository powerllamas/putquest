# -*- coding: utf-8 -*-
# quest/urls.py
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'quest.views.index'),
    (r'^questionnaire/(?P<quest_id>\d+)/', 'quest.views.questionnaire'),
)
