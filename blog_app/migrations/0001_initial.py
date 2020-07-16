# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], verbose_name='状态', default=1)),
                ('is_nav', models.BooleanField(verbose_name='是否为导航', default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('owner', models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('desc', models.CharField(max_length=1024, blank=True, verbose_name='摘要')),
                ('content', models.TextField(verbose_name='正文', help_text='正文必须为MarkDown格式')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除'), (2, '草稿')], verbose_name='状态', default=1)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('category', models.ForeignKey(verbose_name='分类', to='blog_app.Category')),
                ('owner', models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '文章',
                'ordering': ['-id'],
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='名称')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], verbose_name='状态', default=1)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('owner', models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='blog_app.Tag', verbose_name='标签'),
        ),
    ]
