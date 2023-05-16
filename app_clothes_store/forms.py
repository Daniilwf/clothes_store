from django import forms
from .models import Client
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('country', 'city', 'address')
