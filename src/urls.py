# -*- coding: utf-8 -*-
# urls.py

from django.conf.urls.defaults import patterns, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('quest.urls')),
    (r'^accounts/', include('accounts.urls')),
)

urlpatterns += staticfiles_urlpatterns()
