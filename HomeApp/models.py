from django.db import models

# Create your models here.

class APPLIST(models.Model): 
    title = models.CharField(max_length=10,unique=True,verbose_name=u'标题')
    imgurl = models.ImageField(upload_to='static/images',verbose_name=u'图片地址')
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