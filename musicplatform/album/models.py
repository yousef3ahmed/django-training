from email.policy import default
from tokenize import blank_re
from django.db import models
from model_utils.models import TimeStampedModel
from artists.models import Artist
from imagekit.models import ImageSpecField
from django.core.exceptions import ValidationError
from django import forms


class Album( TimeStampedModel ):  
    artist = models.ForeignKey( Artist , on_delete = models.CASCADE )
    name = models.CharField( max_length = 200 , default = "New Album"  ,  verbose_name = "New Album"  )
    cost = models.DecimalField( max_digits = 20 , decimal_places = 2  )
    album_is_approved  = models.BooleanField( default = True , help_text = " Approve the album if its name is not explicit" )
    release  = models.DateTimeField(blank = False)
    def __str__(self) -> str:
        return "Name = " + self.name + " <----------------------> Artist = " + self.artist.Stage


class Song( models.Model ):
    album = models.ForeignKey( Album , on_delete = models.CASCADE )
    name = models.CharField( max_length = 200  , blank  = True , help_text = "if no name is provided, the song's name defaults to the album name" )
    img = models.ImageField( blank  = False )
    thumbnail = ImageSpecField(format='JPEG')    
    
    def save(self, *args, **kwargs):
        if self.name == "":
            self.name = self.album.name
        super(Song, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if(self.album.Song_set.all().count() >1):
            super(Song, self).delete(*args, **kwargs)
        else:
            raise ValidationError("album has only 1 song , can't be deleted")