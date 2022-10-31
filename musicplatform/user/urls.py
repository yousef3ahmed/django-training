from django.urls import path
from . import views

urlpatterns = [
     path('api_detail/<int:pk>',  views.api_detail.as_view()  , name='API DETAIL'),
]