from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from . import models
# Create your views here.
# 登陆
def Landing(request):
    context = {}  
    context['motto_data'] = motto_text()
    name = request.POST.get('name')
    password = request.POST.get('password')
    context['message'] = "请登陆您的账号"
    try:
        User_mi = models.User.objects.get(name=name)
        user_data = models.User_Information.objects.get(userID = User_mi.pk)
    except:
        context['message'] = "用户信息不存在！"
        return render(request,'Landing/Landing.html',context)
    if User_mi.password == password:
        request.session['user_name'] = User_mi.name
        request.session['user_ID'] = User_mi.pk
        request.session['user_miname'] = user_data.name
        request.session['user_gender'] = user_data.gender
        request.session['user_experience'] = user_data.experience
        request.session['user_book'] = user_data.bookID.id
        request.session['user_Classroom'] = user_data.ClassroomID.name
        request.session['is_login'] = True
        return HttpResponseRedirect('/')
    else:
        context['message'] = "密码错误！"
        context['user_name'] = name
    return render(request,'Landing/Landing.html',context)
# 登出
def Logout(request):
    context = {}  
    context['motto_data'] = motto_text()
    context['message'] = "请登陆您的账号"
    if not request.session.get('is_login', None):
        return render(request,'Landing/Landing.html',context)  
    request.session.flush()
    context['message'] = "请登陆您的账号"
    return HttpResponseRedirect('/')