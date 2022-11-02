from pyexpat import model
from statistics import mode
from rest_framework import serializers
from user.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password




class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 

    password1 = serializers.CharField( write_only=True, required=True , validators=[validate_password] )
    password2 = serializers.CharField( write_only=True, required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})


    def create(self, validated_data):

        user = User.objects.create_user(  email=validated_data['email'],
                                          username=validated_data['username'],
                                          password = validated_data['password1'] )
        return user
