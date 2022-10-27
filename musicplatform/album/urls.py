from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
     path('createAlbum', login_required( views.create_album.as_view() ) , name='createAlbum'),
]