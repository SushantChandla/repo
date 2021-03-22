from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from blockchainpart.models import Chain

from . import forms
from blockchainpart.forms import ChainCreateForm

def SignUp(request):
    if request.method == 'POST':
        user_form = forms.UserCreateForm(data=request.POST)
        profile_form = forms.UserProfileForm(data=request.POST)
        chain_form = ChainCreateForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            chain = chain_form.save()
            chain.user = user
            chain.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.chain = chain
            profile.save()

            chain.add(ammount_transferred=profile.balance, remaining_balance=profile.balance)
            chain.save()

            return redirect('landing_page')
    else:
        user_form = forms.UserCreateForm()
        profile_form = forms.UserProfileForm()
        chain_form = ChainCreateForm()

    return render (request, 'accounts/signup.html',{
        'user_form':user_form,
        'profile_form':profile_form,
        'chain_form':chain_form,
    })
