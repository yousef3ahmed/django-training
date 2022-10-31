from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
     path( 'api_register' , views.api_register.as_view()  , name = 'API_REGISTER'  ),
     path( 'api_login' , views.api_login.as_view()  , name = 'API_LOGIN'  ),
     path( 'api_logout' , views.api_logout.as_view()  , name = 'API_LOGOUT'  ),
]