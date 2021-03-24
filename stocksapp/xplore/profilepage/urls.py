from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'profilepage'

urlpatterns = [
    url('profile/', views.ProfilePage, name="profilepage"),
]
