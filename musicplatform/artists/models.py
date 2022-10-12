from email.policy import default
from enum import unique
from pyexpat import model
from sre_parse import State
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.core import validators
from django.core.exceptions import ValidationError
from django.db.models.functions import Coalesce

import re
import datetime

with open("./badwords.txt") as f:
    CENSORED_WORDS = f.readlines()


def validate( words ): 
    f = open("./badwords.txt" , "r")
    ls = f.read()
    exist_count = ls.count(words)
    if exist_count > 0:
        raise ValidationError( "album name shouldn't contain inappropriate expressions!!" )


class PollManager(models.Manager):   
 def get_queryset(self):
        return super().get_queryset().order_by( 'Stage' )


# default require
class Artist( models.Model ):
    Stage = models.CharField( max_length = 200 , unique = True , blank = False  )
    Social_link = models.URLField( max_length = 100 , blank = True  )
    def __str__(self) -> str:
        return "Stage = " + self.Stage + " --- Social = " + self.Social_link
   
    objects = PollManager()
   
    def approved_albums(self):
        return self.album_set.filter(album_is_approved=True).count()
        


class Album( models.Model ):
    artist = models.ForeignKey( Artist , on_delete = models.CASCADE )
    name = models.CharField( max_length = 200 , default = "New Album" , verbose_name = "New Album" , validators = [validate] )
    pub_date = models.DateTimeField('date published' , unique = True)
    release = models.DateTimeField('release published')
    cost = models.DecimalField( max_digits = 20 , decimal_places = 2  )
    album_is_approved  = models.BooleanField( default = True , help_text = " Approve the album if its name is not explicit" )

    def __str__(self) -> str:
        return "Name = " + self.name + " --- Artist = " + self.artist.Stage
    
    def save(self, *args, **kwargs):
        f = open("./badwords.txt" , "r")
        ls = f.read()
        exist_count = ls.count(self.name)
        if exist_count > 0:
            raise ValidationError( "album name shouldn't contain inappropriate expressions !!" )

        super(Album, self).save(*args, **kwargs)

    def was_released_today_or_before(self):
        return self.release <= timezone.now() 
    
    def was_released_before_today(self):
        return self.release <= timezone.now() - datetime.timedelta(days=1)