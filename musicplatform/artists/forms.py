from tabnanny import check
from django import forms
from .models import Artist , Album


class AlbumForm(forms.Form):
    artist = forms.CharField( label='artist name', max_length=100)
    name = forms.CharField( )
    cost = forms.DecimalField( max_digits = 20 , decimal_places = 2 )
    album_is_approved = forms.BooleanField(  help_text = " Approve the album if its name is not explicit" )


    def is_valid(self) -> bool:     
        artist = self.data['artist']
        records = Artist.objects.filter( Stage = artist ).count()

        if records == 0 :
          return False

        return super().is_valid()


class ArtistForm( forms.Form ):
    Stage = forms.CharField( )
    Social_link = forms.CharField( )

    def is_valid(self) -> bool:
        name = self.data['Stage']
        records = Artist.objects.filter( Stage = name ).count()
        if records > 0 :
          return False

        return super().is_valid()
   
