from django.shortcuts import render, redirect

def Home (request):
    return redirect('homeapp:homepage')
