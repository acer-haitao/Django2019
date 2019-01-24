# -*- coding: utf-8 -*-
# Time    : '2019/1/2 21:15'
# Author  : HT
# Email   : acer_yuhaitao@163.com
from index.models import Index_img,Img_txt,Title,Content,Person,Netnew
from index.models import Portfolie,Comment163,Lyric163,Music163,Playlist163,Visit
from xadmin import views
from xadmin.sites import site


class VisitAdmin(object):
    list_display = ['visit_browser','visit_ip','visit_address','visit_page','visit_time']
    list_filter = ['visit_time']
    model_icon = 'fa fa-external-link-square'
site.register(Visit,VisitAdmin)

class Comment163Admin(object):
    list_display = ['song_id','txt','author','create_time','liked']
    list_filter = ['song_id']
    model_icon = 'fa fa-bookmark'
site.register(Comment163,Comment163Admin)


class Lyric163Admin(object):
    list_display = ['song_id','txt','create_time']
    list_filter = ['song_id']
    model_icon = 'fa fa-bullseye'
site.register(Lyric163,Lyric163Admin)



class Music163Admin(object):
    list_display = ['song_id','author','playtime','done','has_lyric','create_time','update_time','comment']
    list_filter = ['song_id']
    model_icon = 'fa fa-caret-square-o-up'
site.register(Music163,Music163Admin)


class Playlist163Admin(object):
    list_display = ['title','link','cnt','playcount','sharecount','commentcount','description','tags','dsc','create_time','update_time','done']
    list_filter = ['title']
    model_icon = 'fa fa-newspaper-o'
site.register(Playlist163,Playlist163Admin)

class PortfolieAdmin(object):
    list_display = ['id','img','h2_title','div_url','p_txt','readmore','addtime']
    list_filter = ['addtime']
    model_icon = 'fa fa-plus-square'
site.register(Portfolie,PortfolieAdmin)


class NetnewAdmin(object):
    list_display = ['id','title','txt','song','name','addtime']
    list_filter = ['addtime']
    model_icon = 'fa fa-sign-out'
site.register(Netnew,NetnewAdmin)

class PersonAdmin(object):
    list_display = ['id','title','txt','more_url','more_txt','addtime']
    list_filter = ['addtime']
    model_icon = 'fa fa-street-view'
site.register(Person,PersonAdmin)


class ContentAdmin(object):
    list_display = ['url1','icon','content','more_url','url1_txt','addtime']
    list_filter = ['addtime']
    model_icon = 'fa fa-star-half-o'
site.register(Content,ContentAdmin)

class Img_txtAdmin(object):
    list_display = ['txt1','txt2','txt3','url','addtime']
    list_filter = ['addtime']
    model_icon = 'fa fa-window-restore'
site.register(Img_txt,Img_txtAdmin)

class TitleAdmin(object):
    list_display = ['title','url','addtime',"class_blank"]
    list_filter = ['title']
    model_icon = 'fa fa-unsorted '
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
