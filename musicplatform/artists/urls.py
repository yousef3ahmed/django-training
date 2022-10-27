from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
     path('createArtists', login_required( views.create_artist.as_view() ) , name='createArtists'),
     path('', views.list_artist.as_view() , name='list'),
]