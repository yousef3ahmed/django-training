from email.policy import default
from enum import unique
from pyexpat import model
from sre_parse import State
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.core import validators
from django.core.exceptions import ValidationError
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


# default require
class Artist( models.Model ):
    Stage = models.CharField( max_length = 200 , unique = True , blank = False  )
    Social_link = models.URLField( max_length = 100 , blank = True  )
    def __str__(self) -> str:
        return "Stage = " + self.Stage + " --- Social = " + self.Social_link
    
   


class Album( models.Model ):
    artist = models.ForeignKey( Artist , on_delete = models.CASCADE )
    name = models.CharField( max_length = 200 , default = "New Album" , verbose_name = "New Album" , validators = [validate] )
    pub_date = models.DateTimeField('date published' , unique = True)
    release = models.DateTimeField('release published')
    cost = models.DecimalField( max_digits = 20 , decimal_places = 2  )
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