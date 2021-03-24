from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r"login/$", views.Login, name="login"),
    url(r"logout/$", views.Logout, name="logout"),
    url(r"signup/$", views.SignUp, name='signup'),
]
