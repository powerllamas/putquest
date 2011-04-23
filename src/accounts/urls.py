# -*- coding: utf-8 -*-
# accounts/urls.py
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    (r'^login/', 'django.contrib.auth.views.login'),
    (r'^logout/', 'django.contrib.auth.views.logout'),
    url(r'^register/', 'accounts.views.register', name='register'),
)
