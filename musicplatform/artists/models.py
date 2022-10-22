from email.policy import default
from enum import unique
from pyexpat import model
from sre_parse import State
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from model_utils.models import TimeStampedModel



class Artist( models.Model ):
    Stage = models.CharField( max_length = 200 , unique = True , blank = False  )
    Social_link = models.URLField( max_length = 100 , blank = True  )

    def __str__(self) -> str:
        return "Stage = " + self.Stage + " <----------------------> Social = " + self.Social_link
   
    def approved_albums(self):
        return self.album_set.filter(album_is_approved=True).count()
        


class Album( TimeStampedModel ):
    
    artist = models.ForeignKey( Artist , on_delete = models.CASCADE )
    name = models.CharField( max_length = 200 , default = "New Album"  ,  verbose_name = "New Album"  )
    cost = models.DecimalField( max_digits = 20 , decimal_places = 2  )
    album_is_approved  = models.BooleanField( default = True , help_text = " Approve the album if its name is not explicit" )
    release  = models.DateTimeField(blank = False)
    def __str__(self) -> str:
        return "Name = " + self.name + " <----------------------> Artist = " + self.artist.Stage
    