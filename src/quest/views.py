# -*- coding: utf-8 -*-

from django.http import Http404
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from quest.models import Questionnaire, Question
from quest.forms import QuestForm, QuestionForm, ChoiceFormSet

def index(request):
    quests = Questionnaire.objects.all()
    context = RequestContext(request)
    return render_to_response('index.html', {'quests': quests}, context_instance=context)

def questionnaire(request, quest_id):
    quest = get_object_or_404(Questionnaire, pk=quest_id)
    questions = Question.objects.filter(questionnaire=quest.pk).order_by('number')
    context = RequestContext(request)
    return render_to_response('questionnaire_view.html', {'quest': quest, 'questions': questions }, context_instance=context)

@login_required
def questionnaire_new(request):
    if request.method == 'POST':
        form = QuestForm(request.POST)
        if form.is_valid():
            quest = form.save()
            quest.owner = request.user
            quest.save()
            return redirect("questionnaire_edit", quest_id=quest.pk)
    else:
        user = request.user
        quest = Questionnaire(owner=user)
        form = QuestForm(instance=quest)

    context = RequestContext(request)
    return render_to_response('questionnaire_new.html',
            {'form': form, },
            context_instance=context)

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
            {'form': form, 'quest': quest, 'questions': questions, },
            context_instance=context)

@login_required
def question_edit(request, quest_id, question_id):
    return question_modify(request, quest_id, question_id, 'question_edit.html')

@login_required
def question_new(request, quest_id):
    return question_modify(request, quest_id, None, 'question_new.html')

@login_required
def question_modify(request, quest_id, question_id, template):
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
                return redirect("questionnaire_edit", quest_id=quest.pk)
            else:
                return redirect("question_edit", quest_id=quest.pk, question_id=question.pk)
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
    return render_to_response('questionnaires_my.html', {'quests': quests}, context_instance=context)


