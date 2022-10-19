from django import forms
from dataclasses import field
from django.forms import ModelForm
from .models import Artist , Album
from datetime import datetime
from .widget import MyDateTimeInput

class AlbumForm(ModelForm):
    
    class Meta:
       model = Album
       fields = '__all__'
       widgets = {
            'release' : MyDateTimeInput()
        }


class ArtistForm (ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'

    def is_valid(self) -> bool:
        name = self.data['Stage']
        records = Artist.objects.filter( Stage = name ).count()
        if records > 0 :
          return False

        return super().is_valid()
   
