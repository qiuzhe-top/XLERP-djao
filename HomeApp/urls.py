from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.postdata, name='postdata'),
    path('warehouse/', views.warehouse, name='warehouse'),
    path('User_picture/', views.User_picture, name='User_picture'),
    # path('postAJ/', views.postAJ, name='postAJ'),
    path('postList/', views.postList, name='postList'),
    path('App/', views.App, name='App'),

]