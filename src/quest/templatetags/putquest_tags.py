# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.filter(name="format_user")
def format_user(user):
    if user.first_name and user.last_name:
        return "%s %s" % (user.first_name, user.last_name)
    else:
        return user.username
