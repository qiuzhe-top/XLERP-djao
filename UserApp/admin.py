from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(UsPicture)
class UsPictureTeleAdmin(admin.ModelAdmin):
    list_display = ('id','UserID')
@admin.register(User_Information)
class User_InformationTeleAdmin(admin.ModelAdmin):
    list_display = ('id','username','name','ClassID','experience')

@admin.register(Unit_class)
class Unit_classTeleAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(User_Sign)
class User_SignTeleAdmin(admin.ModelAdmin):
    list_display = ('id','User_ID','star_time')
    date_hierarchy = ('star_time')    # 详细时间分层筛选　

    