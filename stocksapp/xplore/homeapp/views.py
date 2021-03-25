from django.shortcuts import render, redirect

#from .forms import StockBuyForm
from django.contrib.auth import get_user_model
from datetime import datetime
from homeapp.models import OrgStocks,PriceChange,Stocktype
from datetime import datetime
#User = get_user_model()

# Create your views here.

def HomePage(request):
    allorgStock=OrgStocks.objects.all()
    allorgData=[]
    for i in allorgStock:
        if i.stockAmount!=0:
            stoc=i.stockType
            pricecha=[]
            prices= PriceChange.objects.filter(is_linked=stoc)
            for itme in prices:
                pricecha.append(itme)
            #pricecha.sort(key=lambda item:item.updatedAt)
            newest_price=pricecha[-1].price
            lastPrice=1
            # if pricecha.count >=2:
            #     lastPrice=pricecha[1]
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

def StockBuy(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login.html')
    else:
        if request.method == 'POST':
            username = request.user.username
            stockid_in = request.option
            quantity = request.fname
            quantity=int(quantity)
            stockt=Stocktype.objects.get(stockId=stockid_in)
            orData=OrgStocks.objects.get(stockType=stockt)

            price = PriceChange.objects.filter(is_linked=stockt)
            paymentAmount=request.payment
            pyt =pytezos.using(key="edskRotpJzJHWX4zLsbuyfVnjeojJ3pmysGJEuXSvQWSvBqG1mS4x24TFjQhpiZQpKYNhzJT1DMfXbAE2YKVcuZE6fniECGeRB",shell="https://edonet.smartpy.io")
            contr=pyt.contract("KT1QNvidZC8e5U2UNnv72LUpDtoKfhzu1dge")
            
            

            contr.addTransaction(
                username=username,
                stockType=stockid_in,
                price=paymentAmount,
                quantity=quantity,
                to_from=stockt.stockName+" Organization"
            ).operation_group.sign().inject()

            return redirect('homeapp:homepage')
        else:
            return redirect('homeapp:homepage')


            # stockbuyform = StockBuyForm(data=request.POST)
            # if stockbuyform.is_valid():
            #     stockbuyform.save()

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