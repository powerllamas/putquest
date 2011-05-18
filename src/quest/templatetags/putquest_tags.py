# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.filter(name="format_user")
def format_user(user):
    if user.first_name and user.last_name:
        return "%s %s" % (user.first_name, user.last_name)
    else:
        return user.username

@register.inclusion_tag("form_snippet.html")
def show_form(form):
    return {'form': form }

@register.inclusion_tag("formset_snippet.html")
def show_formset(formset):
    return {'formset': formset }
