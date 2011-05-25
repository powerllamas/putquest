# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from annoying.functions import get_object_or_None

from quest.models import Questionnaire, Question, AnswerSet
from quest.forms import QuestForm, QuestionForm, ChoiceFormSet

def index(request):
    quests = Questionnaire.objects.all()
    context = RequestContext(request)
    return render_to_response('quest/index.html', {'quests': quests}, context_instance=context)

def questionnaire(request, quest_id):
    quest = get_object_or_404(Questionnaire, pk=quest_id)
    questions = Question.objects.filter(questionnaire=quest.pk).order_by('number')
    context = RequestContext(request)
    return render_to_response('quest/questionnaire_view.html', {'quest': quest, 'questions': questions }, context_instance=context)

@login_required
def questionnaire_modify(request, quest_id=None, template='quest/questionnaire_modify.html'):
    if quest_id is None:
        quest = Questionnaire(owner=request.user)
        questions = None
    else:
        quest = get_object_or_404(Questionnaire, pk=quest_id, owner=request.user)
        questions = Question.objects.filter(questionnaire=quest.pk).order_by('number')

    if request.method == 'POST':
        form = QuestForm(request.POST, instance=quest)
        if form.is_valid():
            quest = form.save()
            quest.owner = request.user
            quest.save()
            return redirect("quest.views.questionnaire_modify", quest_id=quest.pk)
    else:
        form = QuestForm(instance=quest)

    context = RequestContext(request)
    return render_to_response(template,
            {'form': form, 'quest': quest, 'questions': questions, },
            context_instance=context)

@login_required
def question_modify(request, quest_id, question_id=None, template='quest/question_modify.html'):
    quest = get_object_or_404(Questionnaire, pk=quest_id, owner=request.user)
    if question_id is None:
        question = Question()
    else:
        question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        formset = ChoiceFormSet(request.POST, instance=question)
        if form.is_valid() and formset.is_valid():
            if question_id is None:
                question = form.save()
                question.questionnaire = quest
                question.save()
            else:
                form.save()
            formset.save()
            if 'action:save' in request.POST:
                return redirect("quest.views.questionnaire_modify", quest_id=quest.pk)
            else:
                return redirect("quest.views.question_modify", quest_id=quest.pk, question_id=question.pk)
    else:
        form = QuestionForm(instance=question)
        formset = ChoiceFormSet(instance=question)

    context = RequestContext(request)
    return render_to_response(template, 
            {'form': form, 'formset': formset, 'quest': quest}, context_instance=context)

@login_required
def questionnaires_my(request):
    quests = Questionnaire.objects.filter(owner=request.user)
    context = RequestContext(request)
    return render_to_response('quest/questionnaires_my.html', {'quests': quests}, context_instance=context)

def questionnaire_fill(request, quest_id):
    quest = get_object_or_404(Questionnaire, pk=quest_id)
    answer_set = get_object_or_None(AnswerSet, user=request.user)

    context = RequestContext(request)
    return render_to_response('quest/questionnaire_fill.html', {'quest': quest}, context_instance=context)
