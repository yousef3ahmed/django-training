from email.policy import default
from enum import unique
from pyexpat import model
from sre_parse import State
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from user.models import User
from model_utils.models import TimeStampedModel



class Artist( models.Model ):

    user = models.OneToOneField(User, on_delete=models.CASCADE  )
    Stage = models.CharField( max_length = 200 , unique = True , blank = False  )
    Social_link = models.URLField( max_length = 100 , blank = True  )

    def __str__(self) -> str:
        return "Stage = " + self.Stage + " <----------------------> Social = " + self.Social_link
   
    def approved_albums(self):
        return self.album_set.filter(album_is_approved=True).count()
        
