from django.contrib import admin

# Register your models here.
from .models import APPLIST

@admin.register(APPLIST)
class APPLISTeleAdmin(admin.ModelAdmin):
    list_display = ('id','title','msg','PANdomurl','WANdomurl','star_time','last_time','isDelete')