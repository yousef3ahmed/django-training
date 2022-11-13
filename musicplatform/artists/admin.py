from dataclasses import field
from django.contrib import admin
from .models import Artist 


# class TopicArtist( admin.ModelAdmin ):
#  list_display = ( 'Stage' , 'Social_link' , 'approved_albums' )

admin.site.register( Artist  )