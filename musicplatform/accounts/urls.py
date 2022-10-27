from re import template
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import user_login


from . import views

urlpatterns = [
    path('logout', views.logout_view.as_view( ) , name='LOGOUT'),
    path('', user_login.as_view( ) , name='LOGIN'),
]