from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.contrib.auth import login, authenticate
from django.contrib.auth import login, logout
from pytezos import pytezos
from homeapp.models import OrgStocks,PriceChange,Stocktype
# Create your views here.

def ProfilePage(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{
             UserProfile.objects.filter(username=request.user.username),
             
        })
    return redirect('/')


def CustomerProfile (request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    username = request.user.username

   

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('accounts/login.html')
        username = request.user.username
        stockid_in = request.POST.get('stocks')
        print(stockid_in)
        quantity = request.POST.get('fname')
        quantity=int(quantity)
        paymentAmount=request.POST.get("payment")
        
        pyt =pytezos.using(key="edskRotpJzJHWX4zLsbuyfVnjeojJ3pmysGJEuXSvQWSvBqG1mS4x24TFjQhpiZQpKYNhzJT1DMfXbAE2YKVcuZE6fniECGeRB",shell="https://edonet.smartpy.io")
        contr=pyt.contract("KT1QNvidZC8e5U2UNnv72LUpDtoKfhzu1dge")
        data =dict(contr.storage())['stocksTotal']
        user_data={}
        if username in data:
            user_data=data[username]
            
            stockt=Stocktype.objects.get(stockId=stockid_in)
            orData=OrgStocks.objects.filter(stockType=stockt)
            if len(orData)>0:
                orData=orData.first
                if( stockid_in in user_data and quantity<=user_data[stockid_in]):
                    price = PriceChange.objects.filter(is_linked=stockt)
                    orData.stockAmount+=quantity
                    orData.save()
                    quantity*=-1
                    paymentAmount*=-1
                    contr.default(price=int(paymentAmount),quantity=quantity,stockType=stockid_in,to_from="Organization",username=username).inject()
                    print("updaeyde")
                else:
                    print("cantDO")
            else:
                print("cantDo")   
        else:
            print("cantDo")
        # return error


   
    u = User.objects.get(username=username)
    name = u.userprofile.name
    email = u.email
    date_of_birth = u.userprofile.date_of_birth
    age =u.userprofile.age
    gender = u.userprofile.gender
    profession =u.userprofile.profession
    mobile_number =u.userprofile.mobile_number
    address =u.userprofile.address
    city = u.userprofile.city
    state =u.userprofile.state
    pin_code =u.userprofile.pin_code
    balance = u.userprofile.balance
    pyt =pytezos.using(key="edskRotpJzJHWX4zLsbuyfVnjeojJ3pmysGJEuXSvQWSvBqG1mS4x24TFjQhpiZQpKYNhzJT1DMfXbAE2YKVcuZE6fniECGeRB",shell="https://edonet.smartpy.io")
    contr=pyt.contract("KT1QNvidZC8e5U2UNnv72LUpDtoKfhzu1dge")
    data =dict(contr.storage())
    
    user_data={}
    if username in data['stocksTotal']:
        user_data=data['stocksTotal'][username]

    alloptions=Stocktype.objects.all()
    print(data)
    return render (request, 'profilepage/profile.html', {
        "username":username,
        "email":email,
        'name':name,
        'date_of_birth':date_of_birth,
        'age':age,
        'gender':gender,
        'profession':profession,
        'mobile_number':mobile_number,
        'address':address,
        'city':city,
        'state':state,
        'pin_code':pin_code,
        'balance':balance,
        'stocksData':user_data,
        'allOptions':alloptions
    })