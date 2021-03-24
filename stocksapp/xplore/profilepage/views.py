from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.contrib.auth import login, authenticate
from django.contrib.auth import login, logout

from accounts.models import UserProfile
# Create your views here.

def ProfilePage(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{
             UserProfile.objects.filter(username=request.user.username),
             
        })
    return redirect('/')