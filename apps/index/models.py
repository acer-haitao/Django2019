# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from datetime import datetime
# Create your models here.

class Visit(models.Model):

    visit_browser = models.CharField(max_length=300,default='txt',verbose_name=u'浏览器')
    visit_page = models.CharField(max_length=30,default='index',verbose_name=u'访问页')
    visit_ip = models.CharField(max_length=30,default='192.168.1.1',verbose_name=u'访问IP')
    visit_time = models.DateTimeField(default=datetime.now(),verbose_name=u'访问时间')
    visit_address = models.CharField(max_length=180,default=u'武汉',verbose_name=u'访问地址')
    visit_msg =    models.CharField(max_length=200,default='msg',verbose_name=u'访问信息')
    class Meta:
        verbose_name = u'访问记录'
        verbose_name_plural = verbose_name
		
		
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
    song_id = models.IntegerField(blank=True, null=True,verbose_name=u'主标题')
    txt = models.TextField(blank=True, null=True,verbose_name=u'评论')
    author = models.CharField(max_length=5000, blank=True, null=True,verbose_name='author')
    liked = models.IntegerField(blank=True, null=True,verbose_name=u'评论数')
    create_time = models.DateTimeField(blank=True, null=True,verbose_name=u'时间')

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = verbose_name


class Lyric163(models.Model):
    song_id = models.IntegerField(blank=True, null=True,verbose_name='song_id')
    txt = models.TextField(blank=True, null=True,verbose_name='txt ')
    create_time = models.DateTimeField(blank=True, null=True,verbose_name='create_time')

    class Meta:
        verbose_name = u'歌词'
        verbose_name_plural = verbose_name


class Music163(models.Model):
    song_id = models.IntegerField(blank=True, null=True,verbose_name=u'歌曲ID')
    song_name = models.CharField(max_length=5000, blank=True, null=True,verbose_name='song_name')
    author = models.CharField(max_length=5000, blank=True, null=True,verbose_name='author')
    playtime = models.IntegerField(db_column='playTime', blank=True, null=True,verbose_name='playtime')  # Field name made lowercase.
    done = models.CharField(max_length=255, blank=True, null=True,verbose_name='done')
    has_lyric = models.CharField(max_length=255, blank=True, null=True,verbose_name='has_lyric')
    create_time = models.DateTimeField(blank=True, null=True,verbose_name='create_time')
    update_time = models.DateTimeField(blank=True, null=True,verbose_name='update_time')
    comment = models.IntegerField(blank=True, null=True,verbose_name='comment')

    class Meta:
        verbose_name = u'音乐'
        verbose_name_plural = verbose_name


class Playlist163(models.Model):
    title = models.CharField(max_length=5000, blank=True, null=True,verbose_name='title')
    link = models.CharField(max_length=255, blank=True, null=True,verbose_name='link')
    cnt = models.IntegerField(blank=True, null=True,verbose_name='cnt')
    playcount = models.IntegerField(db_column='playCount', blank=True, null=True,verbose_name='playcount')  # Field name made lowercase.
    sharecount = models.IntegerField(db_column='shareCount', blank=True, null=True,verbose_name='sharecount')  # Field name made lowercase.
    commentcount = models.IntegerField(db_column='commentCount', blank=True, null=True,verbose_name='commentcount')  # Field name made lowercase.
    description = models.TextField(blank=True, null=True,verbose_name='description')
    tags = models.CharField(max_length=255, blank=True, null=True,verbose_name='tags')
    dsc = models.CharField(max_length=255, blank=True, null=True,verbose_name=u'描述')
    create_time = models.DateTimeField(blank=True, null=True,verbose_name=u'创建时间')
    update_time = models.DateTimeField(blank=True, null=True,verbose_name=u'更新时间')
    done = models.CharField(max_length=255, blank=True, null=True,verbose_name=u'完成')

    class Meta:
        verbose_name = u'歌曲列表'
        verbose_name_plural = verbose_name
