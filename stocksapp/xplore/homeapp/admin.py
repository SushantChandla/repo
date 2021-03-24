from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.OrgStocks)
admin.site.register(models.UserStocks)
admin.site.register(models.StocksRecipts)