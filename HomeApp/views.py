from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect,JsonResponse
import json
import os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from UserApp.models import UsPicture

# Create your views here.
# 访问主页
def home(request):
    context = {}
    context['activehome'] = 'fh5co-active'

    
    return render(request,'home.html',context)
# 文章首页

def postdata(request):
    context = {}
    if request.method == 'GET':
        TClist = models.TitleClassification.objects.all()#获取所有文章类型
        IDdata = request.GET.get('id')
        if IDdata == None:
            #######   需要修改的点   ##############
            post = models.dynamic.objects.all().order_by('id')[0:10].values('id','title','imgurl','userID','OtherMsg','star_time')
        else:
            post = models.dynamic.objects.filter(Classid=IDdata).values('id','title','imgurl','userID','OtherMsg','star_time').order_by('id')
        # context['post'] = post
        contact_list = post #models.dynamic.objects.get_queryset().order_by('id')#.values('id','title')
        # print(contact_list)
        paginator = Paginator(contact_list, 8) # Show 25 contacts per page
        # print(paginator)
        page = request.GET.get('page') #request.POST.get('data')
        try:
            contacts = paginator.page(page)
            # print(contacts)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)    
        context['book_list'] = contacts
        context['paginator'] = paginator
        context['CLASSID'] = IDdata
        context['TClist'] = TClist
        context['activedynamic'] = 'fh5co-active'
    return render(request,'dynamic.html',context)
    
# 文章详细页面
def postList(request):
    context = {}
    id = request.GET.get('id')
    context['data'] =  models.dynamic.objects.get(pk = id)
    return render(request,'post.html',context)
#软件收藏 
def App(request):
    context = {}
    context['applist'] = models.APPLIST.objects.all()
    context['activeApp'] = 'fh5co-active'
    return render(request,'App.html',context)  
#物品管理
def warehouse(request):
    context = {}
    context['warehouse'] = models.warehouse.objects.all()
    # print(context['warehouse'])
    context['activehome'] = 'fh5co-active'
    return render(request,'warehouse.html',context)
