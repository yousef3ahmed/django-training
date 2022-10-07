from email.policy import default
from enum import unique
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
import datetime



# default require
class Artist( models.Model ):
    Stage = models.CharField( max_length = 200 , unique = True , blank = False )
    Social_link = models.URLField( max_length = 100 , blank = True  )
    def __str__(self) -> str:
        return "Stage = " + self.Stage + " --- Social = " + self.Social_link


class Album( models.Model ):
    artist = models.ForeignKey( Artist , on_delete = models.CASCADE )
    name = models.CharField( max_length = 200 , default = "New Album" , verbose_name = "New Album" )
    pub_date = models.DateTimeField('date published' , unique = True)
    release = models.DateTimeField('release published')
    cost = models.DecimalField( max_digits = 20 , decimal_places = 2  )
    def __str__(self) -> str:
        return "Name = " + self.name + " --- Artist = " + self.artist.Stage
    
    def was_released_today_or_before(self):
        return self.release <= timezone.now() 
    
    def was_released_before_today(self):
        return self.release <= timezone.now() - datetime.timedelta(days=1)