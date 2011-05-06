# -*- coding: utf-8 -*-
# accounts/views.py

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from accounts.forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/")
    else:
        form = RegisterForm()
    context = RequestContext(request)
    return render_to_response('registration/register.html', {'form': form}, context_instance=context)
