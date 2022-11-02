from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin 
from .forms import CustomUserChangeFrom



@admin.register(User)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeFrom
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'bio']
    fieldsets = UserAdmin.fieldsets + (
        ("User's Bio", {'fields': ('bio',)}),
    )



# Register your models here.
