from django.forms import ModelForm
from .models import StocksRecipts

class StockBuyForm(ModelForm):
    class Meta:
        model = StocksRecipts
        fields = '__all__'