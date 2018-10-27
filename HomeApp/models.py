from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class APPLIST(models.Model): 
    title = models.CharField(max_length=10,unique=True,verbose_name=u'标题')
    imgurl = models.ImageField(upload_to='images/app',verbose_name=u'图片地址')
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
    imgurl = models.ImageField(upload_to='images/post',verbose_name=u'图片地址')
    msg = models.CharField(max_length=300, verbose_name=u'文章信息') 
    post = RichTextUploadingField(verbose_name=u'具体内容') 
    TitleClassificationID = models.ForeignKey('TitleClassification', on_delete=models.CASCADE,verbose_name=u'文章类型')
    OtherMsg = models.CharField(max_length=300, verbose_name=u'简介') 
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')  
    isDelete = models.BooleanField(default=True,verbose_name=u'是否可用') 
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "动态"
        
class TitleClassification(models.Model):
    title = models.CharField(max_length=30,unique=True,verbose_name=u'标题')
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')  
    isDelete = models.BooleanField(default=True,verbose_name=u'是否可用') 
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "文章类型"