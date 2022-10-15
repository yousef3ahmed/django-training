from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Artist , Album
from .forms import AlbumForm , ArtistForm


# Artist.objects.prefetch_related('album_set').all()

def list_artist(request):
    context = {'artist_list' :  Artist.objects.all()}
    return render(request,'artists/fetch.html',context)

def create_artist(request):
    
    def add_artist( Stages , Social_links  ):
        create = Artist( Stage = Stages  , Social_link = Social_links )
        create.save()

    passed = 1
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            Stage = form.cleaned_data['Stage']
            Social_link = form.cleaned_data['Social_link']
            add_artist( Stage , Social_link )
            return HttpResponse("thanks you, the record added successful.")
        else:
            passed = 0

    else:
        form = ArtistForm()

    return render(request, 'artists/add_artist.html', {'form': form , 'ok' : passed} )


def create_album(request):
    
    def add_album( artist , names , costs  , album_is_approveds ):
        art = Artist.objects.get( Stage = artist)
        create = Album( artist = art  , name  = names , cost = costs , album_is_approved = album_is_approveds )
        create.save()

    passed = 1
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            artist = form.cleaned_data['artist']
            name = form.cleaned_data['name']
            cost = form.cleaned_data['cost']
            album_is_approved = form.cleaned_data['album_is_approved']
            add_album( artist , name , cost , album_is_approved )
            return HttpResponse("thanks you, the record added successful.")
        else:
            passed = 0

    else:
        form = AlbumForm()

    return render(request, 'artists/add_album.html', {'form': form , 'ok' : passed} )

