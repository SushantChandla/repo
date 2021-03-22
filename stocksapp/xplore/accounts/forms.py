from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        fields = ("username", "email", "password")
        model = User


class UserProfileForm (forms.ModelForm):
    class Meta:
        fields = '__all__'
        exclude = ['user', 'chain']
        model = models.UserProfile
