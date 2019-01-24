# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from datetime import datetime
# Create your models here.

class Portfolie(models.Model):
    img = models.ImageField(upload_to="portfolie_img/",verbose_name=u'个人图')
    h2_title = models.CharField(max_length=50,default='Tst',verbose_name=u'图片标题')
    div_url = models.CharField(max_length=30,default='#',verbose_name=u'div链接')
    p_txt = models.CharField(max_length=500,default='txt',verbose_name=u'图片文字')
    readmore = models.CharField(max_length=30,default='点击READMORE',verbose_name=u'更多')
    readmore_url = models.CharField(max_length=30,default='#',verbose_name=u'更多链接')
    addtime = models.DateTimeField(default=datetime.now(),verbose_name=u'添加时间')
    class Meta:
        verbose_name = u'产品轮播'
        verbose_name_plural = verbose_name


class Netnew(models.Model):

    title = models.CharField(max_length=50,default='Tst',verbose_name=u'标题')
    title1 = models.CharField(max_length=150,default='Tst',verbose_name=u'标题内容')
    txt = models.CharField(max_length=500,default='txt',verbose_name=u'评论内容')
    name = models.CharField(max_length=30,default='周杰伦',verbose_name=u'姓名')
    song = models.CharField(max_length=30,default='听妈妈的话',verbose_name=u'歌曲')
    song_txt = models.CharField(max_length=30,default='5300',verbose_name=u'评论数')
    addtime = models.DateTimeField(default=datetime.now(),verbose_name=u'添加时间')
    class Meta:
        verbose_name = u'网易评论'
        verbose_name_plural = verbose_name

class Person(models.Model):
    img = models.ImageField(upload_to="person_img/",verbose_name=u'个人图')
    more_txt = models.CharField(max_length=100,default=u'更多',verbose_name=u'more_txt')
    title = models.CharField(max_length=50,default='Tst',verbose_name=u'标题')
    txt = models.CharField(max_length=50,default='txt',verbose_name=u'内容')
    more_url = models.CharField(max_length=30,default='#',verbose_name=u'more_url')
    addtime = models.DateTimeField(default=datetime.now(),verbose_name=u'添加时间')
    class Meta:
        verbose_name = u'个人'
        verbose_name_plural = verbose_name

class Title(models.Model):
    title = models.CharField(max_length=30,default='Test',verbose_name=u'标题')
    addtime = models.DateTimeField(default=datetime.now(),verbose_name=u'添加时间')
    class_blank =  models.CharField(max_length=10,choices=(("_blank","跳出本页"),("_self","本页跳转")),default='_blank',verbose_name=u'跳转')
    url = models.CharField(max_length=300,default='#',verbose_name=u'链接')
    class Meta:
        verbose_name = u'标题表'
        verbose_name_plural = verbose_name

class Content(models.Model):
    url1 = models.CharField(max_length=200,verbose_name=u'链接')
    url1_txt = models.CharField(max_length=100,default=u'内容XXXX',verbose_name=u'标题')
    content = models.CharField(max_length=200,default=u'内容XXXX',verbose_name=u'内容')
    more_url = models.CharField(max_length=200,default='#',verbose_name=u'More')
    icon = models.CharField(max_length=30,default='icon1',verbose_name=u'样式')
    more_txt =  models.CharField(max_length=30,default= "More",verbose_name=u'More_txt')
    addtime = models.DateTimeField(default=datetime.now(),verbose_name=u'添加时间')
    class Meta:
        verbose_name = u'四模块'
        verbose_name_plural = verbose_name

class Index_img(models.Model):
    addtime = models.DateTimeField(default=datetime.now(),verbose_name=u'添加时间')
    img = models.ImageField(upload_to="index_img/",verbose_name=u'轮播图')
    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name


class Img_txt(models.Model):
    txt1 = models.CharField(max_length=500,verbose_name=u'主标题')
    txt2 = models.CharField(max_length=200,verbose_name=u'副标题')
    txt3 = models.CharField(max_length=50,verbose_name=u'跳转标题')
    url = models.CharField(max_length=30,verbose_name=u'链接')
    addtime = models.DateTimeField(default=datetime.now(),verbose_name=u'添加时间')
    class Meta:
        verbose_name = u'图片下标题'
        verbose_name_plural = verbose_name

class Comment163(models.Model):
    song_id = models.IntegerField(blank=True, null=True)
    txt = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=5000, blank=True, null=True)
    liked = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment163'


class Lyric163(models.Model):
    song_id = models.IntegerField(blank=True, null=True)
    txt = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lyric163'


class Music163(models.Model):
    song_id = models.IntegerField(blank=True, null=True)
    song_name = models.CharField(max_length=5000, blank=True, null=True)
    author = models.CharField(max_length=5000, blank=True, null=True)
    playtime = models.IntegerField(db_column='playTime', blank=True, null=True)  # Field name made lowercase.
    done = models.CharField(max_length=255, blank=True, null=True)
    has_lyric = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    comment = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'music163'


class Playlist163(models.Model):
    title = models.CharField(max_length=5000, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    cnt = models.IntegerField(blank=True, null=True)
    playcount = models.IntegerField(db_column='playCount', blank=True, null=True)  # Field name made lowercase.
    sharecount = models.IntegerField(db_column='shareCount', blank=True, null=True)  # Field name made lowercase.
    commentcount = models.IntegerField(db_column='commentCount', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    dsc = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    done = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playlist163'
