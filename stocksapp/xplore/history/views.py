from django.shortcuts import render,redirect
#from homeapp.models import StocksRecipts
from django.contrib.auth import get_user_model
from pytezos import pytezos
User = get_user_model()
from homeapp.models import Stocktype
# Create your views here.
def UserHistory (request):
    if not request.user.is_authenticated:
      return redirect('accounts:login')
    user_name = request.user.username
    pyt =pytezos.using(key="edskRotpJzJHWX4zLsbuyfVnjeojJ3pmysGJEuXSvQWSvBqG1mS4x24TFjQhpiZQpKYNhzJT1DMfXbAE2YKVcuZE6fniECGeRB",shell="https://edonet.smartpy.io")
    contr=pyt.contract("KT1QNvidZC8e5U2UNnv72LUpDtoKfhzu1dge")
    data =dict(contr.storage())['allTransaction']
    print(data)
    history=[]
    data_set=[]
    if user_name in data:
      history=data[user_name]
    for item in history:
      stock = Stocktype.objects.filter(stockId=item['stockType'])
      if len(stock)> 0 :
        stod=stock[0]
        data_set.append({
          'stockID': stod.stockId,
          'stockName':stod.stockName,
          'price':abs(int(item['price'])),
          'to_from':item['to_from'],
          'is_sold':int(item['quantity'])>0 if False else True,
          'quantity':abs(int(item['quantity'])),
          'time':item["time"]
        })
    return render(request,'history/history.html',{'historyList':data_set})
 

"""
#def UserHistorySelling (request):
#    return redirect("homepage:home")
   
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
    """