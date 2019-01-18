from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.postdata, name='postdata'),
    path('warehouse/', views.warehouse, name='warehouse'),
    path('SigninAjax/', views.SigninAjax, name='SigninAjax'),
    path('postList/', views.postList,  name='postList'),
    path('App/', views.App, name='App'),


    path('login/', views.Landing, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('adduser/', views.adduser, name='adduser'),

]