from django.db import models

class User_Information(models.Model): 
    GENDER_CHOICES = (
        (u'男', u'男'),
        (u'女', u'女'),
    )
    username = models.CharField(max_length=128,unique=True)#账号
    password = models.CharField(max_length=256)#密码
    name = models.CharField(max_length=30, verbose_name=u'姓名') 
    gender = models.CharField(max_length=30, verbose_name=u'性别', choices=GENDER_CHOICES) 
    experience = models.IntegerField(verbose_name=u'经验') 
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')  
    isDelete = models.BooleanField(default=True,verbose_name=u'是否可用') 
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "用户信息"