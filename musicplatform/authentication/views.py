from django.contrib.auth import login, logout

from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse , JsonResponse
from user.models import User

from .serializers import RegisterSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken , TokenAuthentication


from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny , IsAuthenticated


class api_register( APIView ):
    
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class api_login( APIView ):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        _, token = AuthToken.objects.create(user)
        return Response({
            'token': token,
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'bio': user.bio
            },
        })

class api_logout( APIView ):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
         
        if request.user.is_authenticated:
            logout(request)
            return Response({ 'mass' : ' i am logout now.' })
         
        return Response({ 'mass' : 'you are already logout.' })


