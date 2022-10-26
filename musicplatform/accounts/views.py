from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render

from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView



class logout_view( FormView ):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponse("thanks you, i am logout successful.")



class user_login( FormView ):
    form = AuthenticationForm()

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html' , { 'form' : self.form })


    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("thanks you, i am login successful.")
        else:
            return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.' , 'form' : self.form } )

