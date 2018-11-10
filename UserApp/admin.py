from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Userpicture)
class Userpicturedmin(admin.ModelAdmin):
    list_display = ('id','name')

