from dataclasses import field
from django.contrib import admin
from .models import  Album , Song


class TopicAlbum( admin.ModelAdmin ):
 readonly_fields=('created',)

# class TopicSong( admin.ModelAdmin ):
#     readonly_fields=('thumbnail',)

admin.site.register( Song )
admin.site.register( Album , TopicAlbum )