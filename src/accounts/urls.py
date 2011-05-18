# -*- coding: utf-8 -*-
# accounts/urls.py

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^login/', 'django.contrib.auth.views.login', {}, name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/',}, name = 'logout'),
    url(r'^register/', 'accounts.views.register', {}, name='register'),
    url(r'^edit/', 'accounts.views.edit', {}, name='account_edit'),
)
