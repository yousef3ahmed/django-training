from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Artist , Album
from .forms import AlbumForm , ArtistForm


def list_artist(request):
    context = {'artist_list' :  Artist.objects.all()}
    return render(request,'artists/fetch.html',context)

def create_artist(request):
    
    passed = 1
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():

            form.save()
            return HttpResponse("thanks you, the record added successful.")
        else:
            passed = 0

    else:
        form = ArtistForm()

    return render(request, 'artists/add_artist.html', {'form': form , 'ok' : passed} )


def create_album(request):
    
    passed = 1
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("thanks you, the record added successful.")
        else:
            passed = 0

    else:
        form = AlbumForm()

    return render(request, 'artists/add_album.html', {'form': form , 'ok' : passed} )

