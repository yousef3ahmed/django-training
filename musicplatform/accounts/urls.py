from re import template
from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path('logout', views.logout_view, name='LOGOUT'),
    path('', auth_views.LoginView.as_view( template_name = 'login.html' ) , name='LOGIN'),
]