from django.shortcuts import render
from homeapp.models import StocksRecipts
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def UserHistoryBuying (request):
    user_name = User.username
    temp_list = StocksRecipts.objects.all().filter(buyer=user_name)

    stockType_list = []
    buyer_list = []
    amount_list = []
    quantity_list = []
    soldAt_list = []

    if (temp_list):
        for item in temp_list:
            stock_type = item.stockType
            stockType_list.append(stock_type)
            buyer = item.buyer
            buyer_list.append(buyer)
            amount = item.amount
            amount_list.append(amount)
            quantity = item.quantity
            quantity_list.append(quantity)
            soldAt = item.soldAt

    main_list = zip (stockType_list, buyer_list, amount_list, quantity_list, soldAt_list)

    return render(request, 'history/history.html', {'main_list':main_list, 'buyer':user_name })

def UserHistorySelling (request):
    user_name = User.username
    temp_list = StocksRecipts.objects.all().filter(seller=user_name)

    stockType_list = []
    buyer_list = []
    amount_list = []
    quantity_list = []
    soldAt_list = []

    if (temp_list):
        for item in temp_list:
            stock_type = item.stockType
            stockType_list.append(stock_type)
            buyer = item.buyer
            buyer_list.append(buyer)
            amount = item.amount
            amount_list.append(amount)
            quantity = item.quantity
            quantity_list.append(quantity)
            soldAt = item.soldAt

    main_list = zip (stockType_list, buyer_list, amount_list, quantity_list, soldAt_list)

    return render(request, 'history/history.html', {'main_list':main_list, 'seller':user_name})
