from django import forms


class NameForm(forms.Form):
    artist = forms.CharField( label='artist name', max_length=100)
    name = forms.CharField( )
    cost = forms.DecimalField( max_digits = 20 , decimal_places = 2 )
    approved = forms.BooleanField(  help_text = " Approve the album if its name is not explicit" )


   
