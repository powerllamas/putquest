# -*- coding: utf-8 -*-

from models import QuestionOpen, QuestionSingle, QuestionMulti

question_types = {
            'open': ('pytanie otwarte', QuestionOpen),
            'single_selection': ('pojedynczy wybór', QuestionSingle),
            'multi_selection': ('wielokrotny wybór', QuestionMulti),
        }
