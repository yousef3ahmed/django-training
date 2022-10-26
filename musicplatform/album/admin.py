from dataclasses import field
from django.contrib import admin
from .models import  Album , Song
from django.core.exceptions import ValidationError





class SongInline(admin.StackedInline):
    model= Song
    extra= 0
    min_num = 1



class TopicAlbum( admin.ModelAdmin ):
 readonly_fields=('created',)
 inlines=[SongInline]


admin.site.register( Song )
admin.site.register( Album , TopicAlbum )