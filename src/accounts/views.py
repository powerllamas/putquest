# -*- coding: utf-8 -*-
# accounts/views.py

from django.shortcuts import render_to_response
from django.template import RequestContext

def register(request):
    context = RequestContext(request)
    return render_to_response('registration/register.html', {}, context_instance=context)
