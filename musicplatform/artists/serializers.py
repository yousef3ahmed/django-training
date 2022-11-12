from pyexpat import model
from statistics import mode
from rest_framework import serializers
from artists.models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Artist
        fields = '__all__'

    
    def create(self, validated_data):

        # user = Artist.objects.create(  Stage = validated_data['Stage'],
        #                                 Social_link=validated_data['Social_link'] )
        # return user
        return Artist.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        """
        Update and return an existing `Artist` instance, given the validated data.
        """
        instance.Stage = validated_data.get('Stage', instance.Stage)
        instance.Social_link = validated_data.get('Social_link', instance.Social_link)
        instance.save()
        return instance