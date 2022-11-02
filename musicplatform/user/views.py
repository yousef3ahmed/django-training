from django.shortcuts import get_object_or_404
from knox.auth import AuthToken , TokenAuthentication
from rest_framework.views import APIView
from django.http import HttpResponse , JsonResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny , IsAuthenticated


# Create your views here.


class api_detail( APIView ):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get( self, request, pk , **kwargs ):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)