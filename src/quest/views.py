# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render_to_response

from quest.models import Questionnaire

class IndexView(TemplateView):
    template_name = "index.html"

def questionnaire(request, quest_id):
    quest = get_object_or_404(Questionnaire, pk=quest_id)
    return render_to_response('questionnaire_new.html', {'quest': quest})

