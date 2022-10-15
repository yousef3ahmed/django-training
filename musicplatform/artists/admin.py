from dataclasses import field
from django.contrib import admin
from .models import Artist , Album

# Register your models here.
from .models import Artist , Album

class InlineAlbum( admin.StackedInline ):
	model = Album
	extra = 1

class TopicAlbum( admin.ModelAdmin ):
 readonly_fields=('created',)

class TopicArtist( admin.ModelAdmin ):
 list_display = ( 'Stage' , 'Social_link' , 'approved_albums' )
 inlines = [ InlineAlbum ] 

admin.site.register( Artist , TopicArtist )
admin.site.register( Album , TopicAlbum )