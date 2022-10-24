from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render

from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth.forms import AuthenticationForm



def logout_view(request):
    logout(request)
    return HttpResponse("thanks you, i am logout successful.")

def user_login(request):

    form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("thanks you, i am login successful.")
        else:
            return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.' , 'form' : form } )
    else:
        return render(request, 'login.html' , { 'form' : form })