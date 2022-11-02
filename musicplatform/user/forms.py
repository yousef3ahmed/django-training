from django.contrib.auth.forms import UserChangeForm
from .models import User
from django import forms


class CustomUserChangeFrom(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields
        widgets = {
            'bio': forms.Textarea
        }