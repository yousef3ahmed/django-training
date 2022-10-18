from email.policy import default
from enum import unique
from pyexpat import model
from sre_parse import State
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


from model_utils.fields import (
    AutoCreatedField,
    AutoLastModifiedField,
    MonitorField,
    StatusField,
    UUIDField,
)


class TimeStampedModel(models.Model):

    created = AutoCreatedField(_('created'))
    release = AutoCreatedField(_('release'))
    modified = AutoLastModifiedField(_('modified'))

    def save(self, *args, **kwargs):

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
        return "Stage = " + self.Stage + " <----------------------> Social = " + self.Social_link
   
    def approved_albums(self):
        return self.album_set.filter(album_is_approved=True).count()
        


class Album( TimeStampedModel ):
    artist = models.ForeignKey( Artist , on_delete = models.CASCADE )
    name = models.CharField( max_length = 200 , default = "New Album"  ,  verbose_name = "New Album"  )
    cost = models.DecimalField( max_digits = 20 , decimal_places = 2  )
    album_is_approved  = models.BooleanField( default = True , help_text = " Approve the album if its name is not explicit" )

    def __str__(self) -> str:
        return "Name = " + self.name + " <----------------------> Artist = " + self.artist.Stage
    