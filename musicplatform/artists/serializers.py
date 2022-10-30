from pyexpat import model
from statistics import mode
from rest_framework import serializers
from artists.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Artist
        fields = ['id', 'Stage', 'Social_link']

    
    def create(self, validated_data):
        """
        Create and return a new `Artist` instance, given the validated data.
        """
        return Artist.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Artist` instance, given the validated data.
        """
        instance.Stage = validated_data.get('Stage', instance.Stage)
        instance.Social_link = validated_data.get('Social_link', instance.Social_link)
        instance.save()
        return instance