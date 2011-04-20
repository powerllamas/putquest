from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'quest.views.index'),
    (r'^questionnaire/(?P<quest_id>\d+)/', 'quest.views.questionnaire'),
    (r'^login/', 'django.contrib.auth.views.login'),
    (r'^logout/', 'django.contrib.auth.views.logout'),
)
