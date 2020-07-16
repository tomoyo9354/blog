# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=2000, verbose_name='内容')),
                ('nickname', models.CharField(max_length=50, verbose_name='昵称')),
                ('website', models.URLField(verbose_name='网站')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], verbose_name='状态', default=1)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('target', models.ForeignKey(verbose_name='评论目标', to='blog_app.Post')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
    ]
