# Generated by Django 2.1.1 on 2018-11-10 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='单位')),
                ('star_time', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('last_time', models.DateTimeField(auto_now=True, verbose_name='最后一次修改日期')),
                ('isDelete', models.BooleanField(default=True, verbose_name='是否可用')),
            ],
            options={
                'verbose_name_plural': '单位',
            },
        ),
        migrations.CreateModel(
            name='User_picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('imgurl', models.ImageField(upload_to='static/images/UserPicture', verbose_name='图片地址')),
                ('msg', models.CharField(max_length=300, verbose_name='简介')),
                ('star_time', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('last_time', models.DateTimeField(auto_now=True, verbose_name='最后一次修改日期')),
                ('isDelete', models.BooleanField(default=True, verbose_name='是否可用')),
            ],
            options={
                'verbose_name_plural': '成员个性签名',
            },
        ),
        migrations.AlterField(
            model_name='user_information',
            name='experience',
            field=models.IntegerField(blank=True, null=True, verbose_name='经验'),
        ),
        migrations.AddField(
            model_name='user_information',
            name='ClassID',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='UserApp.Unit_class', verbose_name='单位'),
            preserve_default=False,
        ),
    ]