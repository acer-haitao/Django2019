# -*- coding: utf-8 -*-
# Time    : '2019/1/2 21:15'
# Author  : HT
# Email   : acer_yuhaitao@163.com
from index.models import Index_img,Img_txt,Title,Content,Person,Netnew
from index.models import Portfolie,Comment163,Lyric163,Music163,Playlist163
from xadmin import views
from xadmin.sites import site

class Comment163Admin(object):
    list_display = ['song_id']
    list_filter = ['song_id']
    model_icon = 'fa fa-address-book-o'
site.register(Comment163,Comment163Admin)

class Lyric163Admin(object):
    list_display = ['song_id']
    list_filter = ['song_id']
    model_icon = 'fa fa-address-book-o'
site.register(Lyric163,Lyric163Admin)

class Music163Admin(object):
    list_display = ['song_id']
    list_filter = ['song_id']
    model_icon = 'fa fa-address-book-o'
site.register(Music163,Music163Admin)

class Playlist163Admin(object):
    list_display = ['title']
    list_filter = ['title']
    model_icon = 'fa fa-address-book-o'
site.register(Playlist163,Playlist163Admin)

class PortfolieAdmin(object):
    list_display = ['id','img','h2_title','div_url','p_txt','readmore','addtime']
    list_filter = ['addtime']
    model_icon = 'fa fa-address-book-o'
site.register(Portfolie,PortfolieAdmin)


class NetnewAdmin(object):
    list_display = ['id','title','txt','song','name','addtime']
    list_filter = ['addtime']
    model_icon = 'fa fa-address-book-o'
site.register(Netnew,NetnewAdmin)

class PersonAdmin(object):
    list_display = ['id','title','txt','more_url','more_txt','addtime']
    list_filter = ['addtime']
    model_icon = 'fa fa-address-book-o'
site.register(Person,PersonAdmin)


class ContentAdmin(object):
    list_display = ['url1','icon','content','more_url','url1_txt','addtime']
    list_filter = ['addtime']
    model_icon = 'fa fa-address-book-o'
site.register(Content,ContentAdmin)

class Img_txtAdmin(object):
    list_display = ['txt1','txt2','txt3','url','addtime']
    list_filter = ['addtime']
    model_icon = 'fa fa-address-book-o'
site.register(Img_txt,Img_txtAdmin)

class TitleAdmin(object):
    list_display = ['title','url','addtime',"class_blank"]
    list_filter = ['title']
    model_icon = 'fa fa-address-book-o'
site.register(Title,TitleAdmin)

class Index_imgAdmin(object):
    list_display = ['addtime','img']
    list_filter = ['addtime']
site.register(Index_img,Index_imgAdmin)


#添加主题功能
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
site.register(views.BaseAdminView, BaseSetting)


#修改头文件及脚本显示
class GlobalSetting(object):
    site_title = "喻晓生后台管理系统"
    site_footer = "http://daydayup11.cn"
    menu_style = "accordion"
site.register(views.CommAdminView, GlobalSetting)