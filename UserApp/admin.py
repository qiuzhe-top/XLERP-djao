from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(UsPicture)
class UsPictureTeleAdmin(admin.ModelAdmin):
    list_display = ('id','UserID')
@admin.register(User_Information)
class User_InformationTeleAdmin(admin.ModelAdmin):
    list_display = ('id','username','name','ClassID','gender','experience')

@admin.register(Unit_class)
class Unit_classTeleAdmin(admin.ModelAdmin):
    list_display = ('id','name')