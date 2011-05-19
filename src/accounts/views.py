# -*- coding: utf-8 -*-
# accounts/views.py

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from accounts.forms import RegisterForm
from accounts.forms import AccountEditForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect("/accounts/login")
    else:
        form = RegisterForm()
    context = RequestContext(request)
    return render_to_response('registration/register.html', {'form': form}, context_instance=context)

@login_required
def edit(request):
    user = request.user
    context = RequestContext(request)
	
    if request.method == 'POST':
        form = AccountEditForm(request.POST, instance = user)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/accounts/edit?edit_succeded=1")
    else:
        form = AccountEditForm(instance = user)
        pass_form = PasswordChangeForm(user=request.user, data=request.POST)
        if "edit_succeded" in request.GET:
            context ['message'] = u"Twoje dane zostały pomyślnie uaktualnione."
    return render_to_response('registration/account_edit.html', {'form': form, 'pass_form' : pass_form,}, context_instance=context)