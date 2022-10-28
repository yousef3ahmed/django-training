from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Artist 
from .forms import ArtistForm
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from artists.models import Artist
from .serializers import ArtistSerializer


class api_artist( APIView ):

    def get(self, request, *args, **kwargs):
        artist = Artist.objects.all()
        serializer = ArtistSerializer( artist, many=True )
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        serializer = ArtistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class list_artist(View):
    template_name = 'artists/fetch.html'

    def get(self, request, *args, **kwargs):
        context = {'artist_list' :  Artist.objects.all()}
        return render(request,self.template_name,context)


class create_artist( View ):
    template_name = 'artists/add_artist.html'

    def post(self, request, *args, **kwargs):
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("thanks you, the record added successful.")
        else:
            return render(request, self.template_name , {'form': form } )

    def get(self, request, *args, **kwargs):
        form = ArtistForm()
        return render(request, self.template_name , {'form': form } )



