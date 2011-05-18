# -*- coding: utf-8 -*-

question_types = {
            'open': ('pytanie otwarte', ),
            'single_selection': ('pojedynczy wybór', ),
            'multi_selection': ('wielokrotny wybór', ),
        }

question_choices = []
for short, data in question_types.iteritems():
    choice = (short, data[0])
    question_choices.append(choice)

