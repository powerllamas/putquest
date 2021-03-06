# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import Http404

from annoying.functions import get_object_or_None

from quest.models import Questionnaire, Question, Answer, AnswerSet
from quest.forms import QuestForm, QuestionForm, ChoiceFormSet

def index(request):
    quests = Questionnaire.objects.filter(published=True, public=True)
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
def questionnaire_delete(request, quest_id):
    quest = get_object_or_404(Questionnaire, pk=quest_id, owner=request.user)

    if request.method == 'POST':
        if 'action:delete' in request.POST:
            quest.set_active(False)
        return redirect("quest.views.questionnaires_my")

    context = RequestContext(request)
    return render_to_response('quest/questionnaire_delete.html', 
            {'quest': quest}, context_instance=context)

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
def question_delete(request, quest_id, question_id):
    quest = get_object_or_404(Questionnaire, pk=quest_id, owner=request.user)
    question = get_object_or_404(Question, pk=question_id, questionnaire=quest.pk)

    if request.method == 'POST':
        if 'action:delete' in request.POST:
            question.set_active(False)
        return redirect("quest.views.questionnaire_modify", quest_id=quest.pk)

    context = RequestContext(request)
    return render_to_response('quest/question_delete.html', 
            {'question': question}, context_instance=context)

@login_required
def questionnaires_my(request):
    quests = Questionnaire.objects.filter(owner=request.user)
    context = RequestContext(request)
    return render_to_response('quest/questionnaires_my.html', {'quests': quests}, context_instance=context)

@login_required
def show_filled_questionnaire(request, answer_set_id):
    answer_set = get_object_or_404(AnswerSet, pk=answer_set_id)
    if request.user not in (answer_set.user, answer_set.questionnaire.owner):
        raise Http404
    questions = Question.objects.filter(questionnaire=answer_set.questionnaire.pk).order_by('number')
    question_parts = []
    for question in questions:
        answer = get_object_or_None(Answer, answer_set=answer_set.pk, question=question.pk)
        question_parts.append((question, answer))
    context = RequestContext(request)
    return render_to_response('quest/show_filled.html', 
            {'answer_set': answer_set, 
                'quest': answer_set.questionnaire, 'question_parts': question_parts }, 
            context_instance=context)

@login_required
def questionnaire_fill(request, quest_id):
    quest = get_object_or_404(Questionnaire, pk=quest_id)
    answer_set = get_object_or_None(AnswerSet, user=request.user, questionnaire=quest)
    if answer_set is None:
        answer_set = AnswerSet(user=request.user, questionnaire=quest)
    else:
        return redirect("show_answer_set", answer_set_id=answer_set.pk)

    questions = Question.objects.filter(questionnaire=quest.pk).order_by('number')
    question_parts = []
    if request.method == 'POST':
        for question in questions:
            QuestionForm = question.get_form_class()
            answer = get_object_or_None(Answer, answer_set=answer_set.pk, question=question.pk)
            form_part = QuestionForm(question, data=request.POST, instance=answer)
            question_parts.append((question, form_part))
        if all(part[1].is_valid() for part in question_parts):
            answer_set.finished = True
            answer_set.save()
            for part in question_parts:
                part[1].save(answer_set)
            return redirect("index")
    else:
        for question in questions:
            QuestionForm = question.get_form_class()
            answer = get_object_or_None(Answer, answer_set=answer_set.pk, question=question.pk)
            form_part = QuestionForm(question, instance=answer)
            question_parts.append((question, form_part))

    context = RequestContext(request)
    return render_to_response('quest/questionnaire_fill.html', 
            {'quest': quest, 'question_parts': question_parts }, 
            context_instance=context)

@login_required
def questionnaire_answers(request, quest_id):
    quest = get_object_or_404(Questionnaire, pk=quest_id, owner=request.user)
    answer_sets = AnswerSet.objects.filter(questionnaire=quest.pk, finished=True)

    context = RequestContext(request)
    return render_to_response('quest/questionnaire_answers.html',
            {'quest': quest, 'answer_sets': answer_sets},
            context_instance=context)

@login_required
def questionnaire_summary(request, quest_id):
    quest = get_object_or_404(Questionnaire, pk=quest_id, owner=request.user)
    answer_sets = AnswerSet.objects.filter(questionnaire=quest.pk, finished=True)

    questions_data = []
    for question in quest.question_set.order_by('number'):
        answers = []
        if question.type == 'open':
            for answer_set in answer_sets:
                answer = answer_set.answer_set.get(question=question).text
                answers.append(answer)
        else:
            for choice in question.questionchoice_set.order_by('order'):
                answer = (choice.name, choice.answer_set.count())
                answers.append(answer)
        question_data = (question, answers)
        questions_data.append(question_data)

    context = RequestContext(request)
    return render_to_response('quest/questionnaire_summary.html', 
            {'quest': quest, 'answer_sets': answer_sets, 'questions': quest.question_set.all,
                'questions_data': questions_data },
            context_instance=context)
