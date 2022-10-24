from django.shortcuts import render
from django.http import HttpResponse
from .forms import AlbumForm
from django.views.generic import View



# Create your views here.
class create_album( View ):
    template_name = 'album/add_album.html'
    
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



