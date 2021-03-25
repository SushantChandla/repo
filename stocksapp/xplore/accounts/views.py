from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.contrib.auth import login, authenticate
#from blockchainpart.models import Chain

from .models import UserProfile
from django.http import response
from . import forms
#from blockchainpart.forms import ChainCreateForm



def SignUp(request):

    if request.method == 'POST':
        user_form = forms.UserCreateForm(data=request.POST)
        profile_form = forms.UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('homeapp:homepage')
    else:
        user_form = forms.UserCreateForm()
        profile_form = forms.UserProfileForm()

    return render (request, 'accounts/signup.html',{
        'user_form':user_form,
        'profile_form':profile_form,
    })
