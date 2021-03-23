from django.shortcuts import render

# Create your views here.

def ProfilePage(request):
    return render(request, 'profilepage/profile.html',{
    })