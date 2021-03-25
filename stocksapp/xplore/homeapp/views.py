from django.shortcuts import render, redirect

#from .forms import StockBuyForm
from django.contrib.auth import get_user_model
from datetime import datetime
from homeapp.models import OrgStocks,PriceChange,Stocktype
from datetime import datetime
from pytezos import pytezos
#User = get_user_model()

# Create your views here.

def HomePage(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('accounts/login.html')
        username = request.user.username
        stockid_in = request.POST.get('stocks')
        print(stockid_in)
        quantity = request.POST.get('fname')
        quantity=int(quantity)
        paymentAmount=request.POST.get("payment")
        stockt=Stocktype.objects.get(stockId=stockid_in)
        orData=OrgStocks.objects.filter(stockType=stockt)
        if len(orData)>0:
            orData=orData.first
            if(quantity<orData.stockAmount):
                price = PriceChange.objects.filter(is_linked=stockt)
                
                pyt =pytezos.using(key="edskRotpJzJHWX4zLsbuyfVnjeojJ3pmysGJEuXSvQWSvBqG1mS4x24TFjQhpiZQpKYNhzJT1DMfXbAE2YKVcuZE6fniECGeRB",shell="https://edonet.smartpy.io")
                contr=pyt.contract("KT1QNvidZC8e5U2UNnv72LUpDtoKfhzu1dge")
                orData.stockAmount-=quantity
                orData.save()
                contr.default(price=int(paymentAmount),quantity=int(quantity),stockType=stockid_in,to_from="Organization",username=username).inject()
                print("updaeyde")
            print("cant DO")
        else :
            print("cantDO")

    allorgStock=OrgStocks.objects.all()
    allorgData=[]
    for i in allorgStock:
        if i.stockAmount!=0:
            stoc=i.stockType
            pricecha=[]
            prices= PriceChange.objects.filter(is_linked=stoc)
            for itme in prices:
                pricecha.append(itme)
            newest_price=pricecha[-1].price
            lastPrice=1
            percentincrease=(newest_price-lastPrice)*100/lastPrice
            
            allorgData.append({
                'stock':stoc.stockName,
                'stockid':stoc.stockId,
                'price':newest_price,
                'percent_increase':percentincrease,
                'available':i.stockAmount
            })

    alloptions=Stocktype.objects.all()
    return render(request, 'homeapp/index.html',{'allorgData':allorgData,'tops':allorgData[0:3],'allOptions':alloptions})


    
    
    



                # quantity = stockbuyform.cleaned_data.get('fname')
                # stockType = stockbuyform.cleaned_data.get('stocks')
                # buyer = stockbuyform.cleaned_data(User.username)
                # seller = stockbuyform.cleaned_data("organization")
                # tag = stockbuyform.cleaned_data("Buy")
                # soldAt = stockbuyform.cleaned_data(datetime.now())
                # amount = stockbuyform.cleaned_data("1000")

                # orgstocktype = OrgStocks.objects.all().filter(stockType = stockType)
                # userstockincrement = UserStocks.objects.all().filter(username= User.username)
        #         if orgstocktype is not None:
        #             orgstocktype.stockNumber -= quantity
        #             userstockincrement.stockNumber += quantity
        #             return redirect('/')

        #         else:
        #             return redirect('/')


                

        #     return redirect('/')

        # else:
        #     stockbuyform = StockBuyForm()
    
        # context = {'stockbuyform' : "stockbuyform"}
        # return render(request, 'index.html', context)