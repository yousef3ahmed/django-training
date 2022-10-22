from django.urls import path

from . import views

urlpatterns = [
     path('createAlbum', views.create_album, name='index'),
     path('createArtists', views.create_artist , name='index'),
     path('', views.list_artist , name='index'),
]