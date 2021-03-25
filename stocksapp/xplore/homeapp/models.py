import json
from django.db import models
from django.db.models.fields import CharField, DateTimeField, EmailField, IntegerField, URLField, TextField

from accounts.models import UserProfile
from django.utils import timezone 
# Create your models here.



class Stocktype(models.Model):
    stockId=models.CharField("stockId",max_length=20,unique=True)
    stockName=models.CharField("stockName",max_length=256)
  #  lastPrice=models.IntegerField('lastPrice',default=0)
  #  newPrice=models.IntegerField('newPrice',default=0)
    def __str__(self):
        return str(self.stockId)+ " "+ str(self.stockName)
    

class PriceChange(models.Model):
    price=models.IntegerField('price',default=0)
    is_linked=models.ForeignKey(Stocktype,on_delete=models.CASCADE)
    updatedAt=models.TimeField('updatedAt',default=timezone.now)

    def __str__(self):
        return str(self.is_linked)+str(self.price)+" "+str(self.updatedAt)
    


class OrgStocks(models.Model):
    stockType = models.OneToOneField(Stocktype,on_delete=models.CASCADE)
    stockAmount = models.IntegerField('stockAmount',default=0)

    def __str__(self):
      return  str(self.stockType)+" "+str(self.stockAmount)


"""
class UserStocks(models.Model):
    class StockType(models.TextChoices):
        StockA = 'A', ('StockA')
        StockB = 'B', ('StockB')
        StockC = 'C', ('StockC')
        StockD = 'D', ('StockD')
        StockE = 'E', ('StockE')
        StockF = 'F', ('StockF')
        StockG = 'G', ('StockG')

    stockType = models.CharField(max_length = 1, choices= StockType.choices)
    username = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stockNumber = IntegerField('stockNumber', default=10000)
    
    def __str__(self):
      return 'StockType'

class StocksRecipts(models.Model):
    class StockType(models.TextChoices):
        StockA = 'A', ('StockA')
        StockB = 'B', ('StockB')
        StockC = 'C', ('StockC')
        StockD = 'D', ('StockD')
        StockE = 'E', ('StockE')
        StockF = 'F', ('StockF')
        StockG = 'G', ('StockG')

    TagChoices  = (
        ( 'Buy', 'Buy'),
        ('Sell', 'Sell'),
    )

    stockType = models.CharField(max_length = 1, choices= StockType.choices)
    seller = models.ForeignKey(UserStocks, on_delete=models.CASCADE, related_name= 'seller_userstock')
    buyer = models.ForeignKey(UserStocks, on_delete=models.CASCADE, related_name= 'buyer_userstock')
    amount=IntegerField('amount',default=0)
    quantity=IntegerField('quantity',default=0)
    soldAt=DateTimeField('dateTime',default=timezone.now, null = False, blank=False,help_text='Format : YYYY-MM-DDThh:mm')
    tag = models.CharField(max_length = 4, null = False, choices = TagChoices)

    def __str__(self):
      return 'StockPurchase'
"""