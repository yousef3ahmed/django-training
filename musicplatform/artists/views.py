from re import template
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Artist , Album
from .forms import AlbumForm , ArtistForm
from django.views.generic import View
from django.contrib.auth.decorators import login_required



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




# @login_required
class create_album( View ):
    template_name = 'artists/add_album.html'
    
    def post(self, request, *args, **kwargs):
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("thanks you, the record added successful.")
        else:
            return render(request, self.template_name , {'form': form } )

    def get(self, request, *args, **kwargs):
        form = AlbumForm()
        return render(request, self.template_name , {'form': form } )

