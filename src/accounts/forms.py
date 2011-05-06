# -*- coding: utf-8 -*-
# accounts/forms.py

from django import forms

class RegisterForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'

    username = forms.CharField(label="Nazwa użytkownika")
    first_name = forms.CharField(label="Imię")
    last_name = forms.CharField(label="Nazwisko")
    email = forms.EmailField(label="Adres email")
