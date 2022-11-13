from pyexpat import model
from statistics import mode
from rest_framework import serializers
from .models import Album
from artists.serializers import ArtistSerializer


class AlbumSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Album
        fields = ['id', 'artist', 'name', 'release', 'cost']
    
    artist = ArtistSerializer(read_only=True)


class AlbumRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Album
        fields = ['name' , 'release' , 'cost']
    
    def create(self, validated_data):
        # this work when i call *save() in my view. 
        return Album.objects.create(name = validated_data['name']
                                   ,release = validated_data['release']
                                   ,cost = validated_data['cost']
                                   ,artist = self.context['artist'])