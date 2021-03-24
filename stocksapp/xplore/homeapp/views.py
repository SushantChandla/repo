from django.shortcuts import render, redirect
from .models import *
from .forms import StockBuyForm
from django.contrib.auth import get_user_model
from datetime import datetime


User = get_user_model()

# Create your views here.

def HomePage(request):
    return render(request, 'homeapp/index.html',{})

def StockBuy(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login.html')
    else:
        if request.method == 'POST':
            stockbuyform = StockBuyForm(data=request.POST)
            if stockbuyform.is_valid():
                stockbuyform.save()

                quantity = stockbuyform.cleaned_data.get('fname')
                stockType = stockbuyform.cleaned_data.get('stocks')
                buyer = stockbuyform.cleaned_data(User.username)
                seller = stockbuyform.cleaned_data("organization")
                tag = stockbuyform.cleaned_data("Buy")
                soldAt = stockbuyform.cleaned_data(datetime.now())
                amount = stockbuyform.cleaned_data("1000")

                orgstocktype = OrgStocks.objects.all().filter(stockType = stockType)
                userstockincrement = UserStocks.objects.all().filter(username= User.username)
                if orgstocktype is not None:
                    orgstocktype.stockNumber -= quantity
                    userstockincrement.stockNumber += quantity
                    return redirect('/')

                else:
                    return redirect('/')


                

            return redirect('/')

        else:
            stockbuyform = StockBuyForm()

        context = {'stockbuyform' : stockbuyform}

        return render(request, 'index.html', context)