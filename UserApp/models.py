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
    experience = models.IntegerField(null=True, blank=True,verbose_name=u'经验')
    ClassID = models.ForeignKey('Unit_class', on_delete=models.CASCADE,verbose_name=u'班级')
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')  
    isDelete = models.BooleanField(default=True,verbose_name=u'是否可用') 
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "用户信息"

class UsPicture(models.Model):
    GENDER_CHOICES = (
        (u'Red', u'红色'),
        (u'Pink', u'粉红色'),
        (u'Purple', u'紫色'),
        (u'Deep-Purple', u'深紫色'),
        (u'Indigo', u'靛蓝'),
        (u'Blue', u'蓝色'),
    )
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name=u'姓名(默认不填)') 
    imgurl = models.ImageField(upload_to='static/images/UserPicture',verbose_name=u'图片地址')
    motto = models.CharField(max_length=100, verbose_name=u'格言') 
    msg = models.CharField(max_length=300, verbose_name=u'简介') 
    LoveColor = models.CharField(max_length=30, verbose_name=u'颜色', choices=GENDER_CHOICES) 
    UserID = models.OneToOneField('User_Information', null=True, blank=True, on_delete=models.CASCADE,verbose_name=u'姓名')
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')  
    isDelete = models.BooleanField(default=True,verbose_name=u'是否可用：') 
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "成员个性签名"

class Unit_class(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'单位') 
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')  
    isDelete = models.BooleanField(default=True,verbose_name=u'是否可用') 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "班级"