# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from quest.models import Questionnaire

def index(request):
    quests = Questionnaire.objects.all()
    context = RequestContext(request)
    return render_to_response('index.html', {'quests': quests}, context_instance=context)

def questionnaire(request, quest_id):
    quest = get_object_or_404(Questionnaire, pk=quest_id)
    context = RequestContext(request)
    return render_to_response('questionnaire_new.html', {'quest': quest}, context_instance=context)

