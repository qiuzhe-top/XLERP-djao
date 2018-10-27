from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect,JsonResponse
import json

# Create your views here.
def home(request):
    context = {}
    context['activehome'] = 'fh5co-active'
    return render(request,'home.html',context)
def postdata(request):
    context = {}
    if request.method == 'GET':
        TClist = models.TitleClassification.objects.all()
        IDdata = request.GET.get('id')
        if IDdata == None:
            post = models.dynamic.objects.all().values('id','title','imgurl','msg','OtherMsg','star_time')[0:3]    #取出id和user列，并生成一个列表
            context['post'] = post
        else:
            post = models.dynamic.objects.filter(id=IDdata)
            context['post'] = post
        context['TClist'] = TClist
        context['activedynamic'] = 'fh5co-active'


    return render(request,'dynamic.html',context)
def postAJ(request):
    context = {}
    data = request.POST.get('data')
    data = int(data)
    print(data)
    a = data * 3+1
    b =  data * 3+3
    post = models.dynamic.objects.filter(id = 1).values('id','title','imgurl','msg','OtherMsg','star_time')[a:b]    #取出id和user列，并生成一个列表
    
    print(json.dumps(list(post)))
    context['post'] = json.dumps(list(post))
    return JsonResponse(context)
    
def postList(request):
    context = {}
    id = request.GET.get('id')
    context['data'] =  models.dynamic.objects.get(pk = id).post
    return render(request,'post.html',context)
    
def App(request):
    context = {}
    context['applist'] = models.APPLIST.objects.all()
    print(context['applist'])
    context['activeApp'] = 'fh5co-active'
    return render(request,'App.html',context)  
# 题目录入页面Tk_add    # 题目保存add_subject  #批量上传页面Tk_add_all