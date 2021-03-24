from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'history'

urlpatterns = [
    url('buyinghistory/', views.UserHistoryBuying, name="buying_history"),
    url('sellinghistory/', views.UserHistorySelling, name="selling_history"),
]
