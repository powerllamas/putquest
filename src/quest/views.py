# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from quest.models import Questionnaire, Question
from quest.forms import QuestForm

def index(request):
    quests = Questionnaire.objects.all()
    context = RequestContext(request)
    return render_to_response('index.html', {'quests': quests}, context_instance=context)

def questionnaire(request, quest_id):
    quest = get_object_or_404(Questionnaire, pk=quest_id)
    context = RequestContext(request)
    return render_to_response('questionnaire_view.html', {'quest': quest}, context_instance=context)

@login_required
def questionnaire_new(request):
    user = request.user
    quest = Questionnaire(name="Nowa ankieta", owner=user)
    quest.save()
    return redirect("questionnaire_edit", quest_id=quest.pk)

@login_required
def questionnaire_edit(request, quest_id):
    quest = get_object_or_404(Questionnaire, pk=quest_id)
    if quest.owner != request.user:
        raise Http404

    if request.method == 'POST':
        form = QuestForm(request.POST, instance=quest)
        if form.is_valid():
            form.save()
            return redirect("questionnaire_edit", quest_id=quest.pk)
    else:
        form = QuestForm(instance=quest)

    questions = Question.objects.filter(questionnaire=quest.pk).order_by('number')
    context = RequestContext(request)
    return render_to_response('questionnaire_edit.html', 
            {'form': form, 'quest': quest, 'questions': questions }, context_instance=context)

def question_edit(request, quest_id, question_id):
    raise Http404

def question_new(request, quest_id):
    raise Http404
