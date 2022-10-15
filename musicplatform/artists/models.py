from email.policy import default
from enum import unique
from pyexpat import model
from sre_parse import State
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


from model_utils.fields import (
    AutoCreatedField,
    AutoLastModifiedField,
    MonitorField,
    StatusField,
    UUIDField,
)



with open("./badwords.txt") as f:
    CENSORED_WORDS = f.readlines()


def validate( words ): 
    f = open("./badwords.txt" , "r")
    ls = f.read()
    exist_count = ls.count(words)
    if exist_count > 0:
        raise ValidationError( "album name shouldn't contain inappropriate expressions!!" )


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created = AutoCreatedField(_('created'))
    release = AutoCreatedField(_('release'))
    modified = AutoLastModifiedField(_('modified'))

    def save(self, *args, **kwargs):
        """
        Overriding the save method in order to make sure that
        modified field is updated even if it is not given as
        a parameter to the update field argument.
        """
        update_fields = kwargs.get('update_fields', None)
        if update_fields:
            kwargs['update_fields'] = set(update_fields).union({'modified'})

        super().save(*args, **kwargs)

    class Meta:
        abstract = True



class Artist( models.Model ):
    Stage = models.CharField( max_length = 200 , unique = True , blank = False  )
    Social_link = models.URLField( max_length = 100 , blank = True  )
    def __str__(self) -> str:
        return "Stage = " + self.Stage + " --- Social = " + self.Social_link
   
    def approved_albums(self):
        return self.album_set.filter(album_is_approved=True).count()
        


class Album( TimeStampedModel ):
    artist = models.ForeignKey( Artist , on_delete = models.CASCADE )
    name = models.CharField( max_length = 200 , default = "New Album" , verbose_name = "New Album" , validators = [validate] )
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
