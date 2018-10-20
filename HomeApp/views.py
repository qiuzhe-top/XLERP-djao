from django.shortcuts import render
from .models import APPLIST

# Create your views here.
def home(request):
    context = {}
    context['activehome'] = 'fh5co-active'
    return render(request,'home.html',context)
def dynamic(request):
    context = {}
    context['activedynamic'] = 'fh5co-active'
    return render(request,'dynamic.html',context)
def App(request):
    context = {}
    
    context['applist'] = APPLIST.objects.all()
    print(context['applist'])
    context['activeApp'] = 'fh5co-active'

    return render(request,'App.html',context)  
# 题目录入页面Tk_add    # 题目保存add_subject  #批量上传页面Tk_add_all