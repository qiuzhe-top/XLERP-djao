from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.postdata, name='postdata'),
    path('postList/', views.postList, name='postList'),
    path('App/', views.App, name='App'),

]