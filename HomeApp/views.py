from django.shortcuts import render
from .models import APPLIST,dynamic
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    context = {}
    context['activehome'] = 'fh5co-active'
    return render(request,'home.html',context)
def postdata(request):
    context = {}
    post = dynamic.objects.all().values('id','title','imgurl','msg','OtherMsg','star_time')    #取出id和user列，并生成一个列表
    print(post)
    context['post'] = post
    context['activedynamic'] = 'fh5co-active'
    return render(request,'dynamic.html',context)
def postList(request):
    context = {}
    id = request.GET.get('id')
    context['data'] =  dynamic.objects.get(pk = id).post
    return render(request,'post.html',context)
    
def App(request):
    context = {}
    context['applist'] = APPLIST.objects.all()
    print(context['applist'])
    context['activeApp'] = 'fh5co-active'
    return render(request,'App.html',context)  
# 题目录入页面Tk_add    # 题目保存add_subject  #批量上传页面Tk_add_all