from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from UserApp.models import User_Information
# Create your models here.

class APPLIST(models.Model): 
    title = models.CharField(max_length=10,unique=True,verbose_name=u'标题')
    imgurl = models.ImageField(upload_to='static/images/app',verbose_name=u'图片地址')
    msg = models.CharField(max_length=300, verbose_name=u'简介') 
    PANdomurl = models.CharField(max_length=300, verbose_name=u'网盘地址') 
    WANdomurl = models.CharField(max_length=300, verbose_name=u'其它地址') 
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')  
    isDelete = models.BooleanField(default=True,verbose_name=u'是否可用') 
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "APP"
    
class dynamic(models.Model): 
    title = models.CharField(max_length=30,unique=True,verbose_name=u'标题')
    imgurl = models.ImageField(upload_to='static/images/post',null=True, blank=True, verbose_name=u'图片地址')
    userID = models.ForeignKey(User_Information,on_delete=models.CASCADE,verbose_name=u'作者') 
    post = RichTextUploadingField(verbose_name=u'具体内容') 
    Classid = models.ForeignKey('TitleClassification', on_delete=models.CASCADE,verbose_name=u'文章类型')
    OtherMsg = models.CharField(max_length=300, verbose_name=u'简介') 
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')  
    isDelete = models.BooleanField(default=True,verbose_name=u'是否可用') 
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "文章"
        
class TitleClassification(models.Model):
    title = models.CharField(max_length=30,unique=True,verbose_name=u'标题')
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')  
    isDelete = models.BooleanField(default=True,verbose_name=u'是否可用') 
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "文章类型"

class warehouse(models.Model):
    title = models.CharField(max_length=100,unique=True,verbose_name="名称")
    numbers = models.IntegerField(null=True, blank=True,verbose_name=u'数量')
    imgurl = models.ImageField(upload_to='static/images/PhotoWall',verbose_name=u'图片地址')
    msg = models.CharField(max_length=300, verbose_name=u'简介') 
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')  
    isDelete = models.BooleanField(default=True,verbose_name=u'是否可用') 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "社团物品"

class PhotoWall(models.Model):
    Myname = models.CharField(max_length=100,unique=True,verbose_name="姓名")
    imgurl = models.ImageField(upload_to='static/images/PhotoWall',verbose_name=u'图片地址')
    msg = models.CharField(max_length=300, verbose_name=u'简介') 
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')  
    isDelete = models.BooleanField(default=True,verbose_name=u'是否可用') 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "照片墙"