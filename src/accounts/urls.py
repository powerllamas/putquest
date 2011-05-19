# -*- coding: utf-8 -*-
# accounts/urls.py

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^login/', 'django.contrib.auth.views.login', {}, name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/',}, name = 'logout'),
    url(r'^register/', 'accounts.views.register', {}, name='register'),
    url(r'^edit/', 'accounts.views.edit', {}, name='account_edit'),
	url(r'^pass_change/', 'django.contrib.auth.views.password_change', {}, name = 'pass_change'),
	url(r'^pass_changed/', 'django.contrib.auth.views.password_change_done', {}, name = 'pass_changed'),
	url(r'^pass_reset/', 'django.contrib.auth.views.password_reset', {}, name = 'pass_reset'),
	url(r'^pass_reset_done/', 'django.contrib.auth.views.password_reset_done', {}, name = 'pass_reset_done'),
	url(r'^pass_reset_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/', 'django.contrib.auth.views.password_reset_confirm', {}, name = 'pass_reset_confirm'),
	url(r'^pass_reset_complete/', 'django.contrib.auth.views.password_reset_complete', {}, name = 'pass_reset_complete'),
)
