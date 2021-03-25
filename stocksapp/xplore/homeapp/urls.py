from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'homeapp'

urlpatterns = [
    url('home/', views.HomePage, name="homepage"),
    # url('stockbuy/', views.StockBuy, name="stockbuy"),
]
    