from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'homeapp'

urlpatterns = [
    url('', views.HomePage, name="homepage"),
]
