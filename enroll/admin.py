from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ('id','firstname','lastname','email','password')