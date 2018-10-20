# Generated by Django 2.1.1 on 2018-10-20 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APPLIST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='标题')),
                ('imgurl', models.ImageField(upload_to='img', verbose_name='图片地址')),
                ('msg', models.CharField(max_length=30, verbose_name='简介')),
                ('LANdomurl', models.CharField(max_length=30, verbose_name='本地地址')),
                ('WANdomurl', models.CharField(max_length=30, verbose_name='网络地址')),
                ('star_time', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('last_time', models.DateTimeField(auto_now=True, verbose_name='最后一次修改日期')),
                ('isDelete', models.BooleanField(default=True, verbose_name='是否可用')),
            ],
            options={
                'verbose_name_plural': 'APP',
            },
        ),
    ]
