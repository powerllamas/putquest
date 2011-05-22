# -*- coding: utf-8 -*-
# accounts/urls.py

from django.conf.urls.defaults import patterns, url

from accounts.forms import PasswordChangeForm, SetPasswordForm, PasswordResetForm

urlpatterns = patterns('',
    url(r'^login/', 'django.contrib.auth.views.login', 
        {
            'template_name': 'accounts/login.html',
        }, name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/',}, name = 'logout'),
    url(r'^register/', 'accounts.views.register', {}, name='register'),
    url(r'^edit/', 'accounts.views.edit', {}, name='account_edit'),

	url(r'^pass_change/', 'django.contrib.auth.views.password_change', 
        {
            'template_name': 'accounts/password_change.html',
            'post_change_redirect': '../edit?password_changed=1',
            'password_change_form': PasswordChangeForm,
        }, name = 'pass_change'),

	url(r'^pass_reset/', 'django.contrib.auth.views.password_reset', 
	    {
            'template_name': 'accounts/password_reset.html',
            'password_reset_form': PasswordResetForm,
	    }, name = 'pass_reset'),

	url(r'^pass_reset_done/', 'django.contrib.auth.views.password_reset_done', 
	    {
            'template_name': 'accounts/password_reset_done_putquest.html',
	    }, name = 'pass_reset_done'),

	url(r'^pass_reset_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/', 'django.contrib.auth.views.password_reset_confirm', 
	    {
            'template_name': 'accounts/password_reset_confirm_putquest.html',
            'post_reset_redirect': '/accounts/login',
            'set_password_form': SetPasswordForm,
	    }, name = 'pass_reset_confirm'),
)
