from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .forms import AlbumForm
from django.views.generic import FormView
from .models import Album, Artist

from django_filters import rest_framework as filters
from .filters import AlbumFilter

from .serializers import AlbumSerializer , AlbumRequestSerializer
from rest_framework.response import Response

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny , IsAuthenticated
from knox.auth import  TokenAuthentication




class api_album( APIView ):

    pagination_class = LimitOffsetPagination
    filterset_class = AlbumFilter
    filter_backends = (filters.DjangoFilterBackend,)

    def get( self ,request, *args, **kwargs ):
        permission_classes = (AllowAny,)
        album = Album.objects.filter( album_is_approved = True )
        serializer = AlbumSerializer( album, many=True )
        return Response(serializer.data, status=200)
    
    def post( self ,request, *args, **kwargs ):
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)

        try:
            artist = Artist.objects.get(user = request.user)
        except :
            return Response(status = 403 )
        

        serializer = AlbumRequestSerializer(data=request.data ,context={'artist': artist})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200 )
        return Response(serializer.errors, status = 400 )


class AlbumListManual(APIView):
    pagination_class = LimitOffsetPagination
    permission_classes = (AllowAny,)

    def get(self, request ,*args, **kwargs):
        lte = request.query_params.get('cost__gte')
        gte = request.query_params.get('cost__lte')
        name = request.query_params.get('name')
       
        queryset = Album.objects.filter(album_is_approved  = True) 

        try:
            if gte is not None:
                queryset = queryset.filter(cost__gte= gte)
            if lte is not None:
                queryset = queryset.filter(cost__lte=lte)
        except:
            raise ValidationError(
                "cost can't be a string you should set it as an integer.")


        if(not name is None):
            queryset = queryset.filter(name__iexact= name).all()
        
        
        
        serializer = AlbumSerializer(queryset, many=True)
        return Response(serializer.data)





# Create your views here.
class create_album( FormView ):
    template_name = 'album/add_album.html'
    form_class = AlbumForm
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("thanks you, the record added successful.")
        else:
            return render(request, self.template_name , {'form': form } )

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name , {'form': form } )



