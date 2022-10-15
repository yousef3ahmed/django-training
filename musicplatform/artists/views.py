from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .forms import NameForm

# Create your views here.

def index(request):
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            artist = form.cleaned_data['artist']
            name = form.cleaned_data['name']
            cost = form.cleaned_data['cost']
            print( name )
            return HttpResponse("Hello, world. You're at the artists index.")
            # return HttpResponseRedirect('/thanks/')

    # # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'artists/add_album.html', {'form': form})

    # return render( request , 'artists/add_album.html' )
    # return HttpResponse("Hello, world. You're at the artists index.")