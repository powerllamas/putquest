# -*- coding: utf-8 -*-
# accounts/forms.py

from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    error_css_class = 'errors'
    required_css_class = 'required'

    first_name = forms.CharField(label="Imię", required=False, max_length=30)
    last_name = forms.CharField(label="Nazwisko", required=False, max_length=30)
    username = forms.RegexField(label="Nazwa użytkownika", regex=r"^[A-Za-z0-9_@+.-]*$",
            error_messages={'invalid': u'Tylko znaki alfanumeryczne oraz _.-+@.'},
            max_length=30)
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput)
    password_repeat = forms.CharField(label="Powtórz hasło", widget=forms.PasswordInput)
    email = forms.EmailField(label="Adres email")

    def clean_username(self):
        try:
            User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(u'Nazwa użytkownika jest już zajęta.')

    def clean_password_repeat(self):
        if 'password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_repeat']:
                raise forms.ValidationError(u'Hasła nie zgadzają się.')
        return self.cleaned_data

    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        email = self.cleaned_data['email']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return user

class AccountEditForm(forms.ModelForm):
    error_css_class = 'errors'
    required_css_class = 'required'
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
