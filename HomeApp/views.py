from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect,JsonResponse
import json
import os
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from UserApp.models import UsPicture,User_Information,User_Sign

# Create your views here.
# 访问主页
def home(request):
    context = {}
    context['activehome'] = 'fh5co-active'
    return render(request,'home.html',context)
def Landing(request):
    context = {}
    # context['motto_data'] = motto_text()
    context['message'] = "请登陆您的账号"
    if request.method=="POST":
        password = request.POST.get('password')
        username = request.POST.get('username')
        try:
            User_mi = User_Information.objects.get(username=username)
            # user_data = User_Information.objects.get(userID = User_mi.pk)
        except:
            context['message'] = "用户信息不存在！"
            return render(request,'login.html',context)
        if User_mi.password == password:
            request.session['user_name'] = User_mi.name
            context['user_name'] = User_mi.name
            request.session['user_ID'] = User_mi.pk
            request.session['user_experience'] = User_mi.experience
            request.session['is_login'] = True
            return HttpResponseRedirect('/')
        else:
            context['message'] = "密码错误！"
            context['user_name'] = username

        return render(request,'login.html',context)
    return render(request,'login.html',context)
# 登出
def Logout(request):
    context = {}  
    if not request.session.get('is_login', None):
        return render(request,'login.html',context)  
    request.session.flush()
    context['user_name'] = '登录'
    return HttpResponseRedirect('/')
# 注册
def adduser(request):
    context = {}  
    context['message'] = '注册'
    context['username'] = '账号'
    context['name'] = '姓名'
    if request.method=="POST":
        if request.POST.get('password') == request.POST.get('passwords'):
            username = request.POST.get('username')
            name = request.POST.get('name')
            try:
                User_Information.objects.get(username=username)
                # user_data = User_Information.objects.get(userID = User_mi.pk)
                context['message'] = '用户已经存在'
                return render(request,'adduser.html',context) 
            except:
                User_Information.objects.create(name = name,password = request.POST.get('password'),username = username)
                User_mi = User_Information.objects.get(username=username)
                request.session['user_name'] = User_mi.name
                context['user_name'] = User_mi.name
                request.session['user_ID'] = User_mi.pk
                request.session['user_experience'] = User_mi.experience
                request.session['is_login'] = True
                return HttpResponseRedirect('/')
        else:
            context['username'] = request.POST.get('username')
            context['name'] = request.POST.get('name')
            context['message'] = '两次密码不一致'
            return render(request,'adduser.html',context)
    return render(request,'adduser.html',context)
# 签到
def SigninAjax(request):
    context = {}
    if request.session.get('is_login', None):
            try:
                user = User_Information.objects.get(id=request.session['user_ID'])
                # user_timer = User_Sign.objects.filter(User_ID=user).order_by('-id')#[0].last_time
                now_day = datetime.datetime.now()
                user_timer = User_Sign.objects.filter(User_ID=user,last_time__year=now_day.year,last_time__month=now_day.month,last_time__day=now_day.day)#.order_by('-id')#[0].last_time
                if user_timer.count() == 0:
                    # user_timer = user_timer[0].last_time.datetime.now()
                    # now_day = datetime.datetime.now()
                    # print(now_day,user_timer)
                    # if now_day.day != user_timer.day and now_day.year != user_timer.year:
                    user = User_Information.objects.get(id=request.session['user_ID'])
                    User_Sign.objects.create(User_ID = user)
                    context['msg'] =  "签到成功"
                else:
                    context['msg'] =  "已经签到"
                # else:
                    # user = User_Information.objects.get(id=request.session['user_ID'])
                    # User_Sign.objects.create(User_ID = user)
                    # context['msg'] =  "签到成功"
            except:
                context['msg'] =  "签到失败"
    json.dumps(context)

    # ip =comment.ip_address=request.META.get("REMOTE_ADDR",None)
    # if request.META.has_key('HTTP_X_FORWARDED_FOR'):
    #     ip =  request.META['HTTP_X_FORWARDED_FOR']
    # else:
    #     ip = request.META['REMOTE_ADDR']
    # print(ip) 
    return JsonResponse(context) 

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
