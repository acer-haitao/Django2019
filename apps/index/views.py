from django.shortcuts import render
from index.models import Title,Index_img,Img_txt,Content,Person,Netnew,Portfolie,Comment163,Visit
from django.views.generic.base import View
# Create your views here.
import datetime
import requests

from twilio.rest import Client

def send_sms(account_sid,auth_token,from_man,to_man,msg):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=to_man,
        from_=from_man,
        body=msg)
    return message.sid

def formatDate(date):
    return datetime.strptime(date, '%Y%m%d').strftime('%Y-%m-%d')
	
	
def getIpAddr(url):
    response = requests.get(url)
    response.encoding=response.apparent_encoding
    content = response.text
    str = content[content.find("WhwtdWrap bor-b1s col-gray03"):content.find("clearfix plr10")-87]
    a = str[::-1]
    b = a[0:a.find(">")]
    return b[::-1]


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')  
    return ip 

class IndexView(View):
    def get(self,request):
        img = Index_img.objects.all()
        title = Title.objects.all()
        img_txt = Img_txt.objects.all()
        content = Content.objects.all()
        person = Person.objects.all()
        #netnew = Netnew.objects.all()
        netnew = Comment163.objects.all().order_by("?")[:3]
        from_num = '+19047478554'
        to_num = '+8613387614207'
        visit_address = getIpAddr("http://ip.tool.chinaz.com/"+get_ip(request))
        msg = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') +  "-From-"+get_ip(request)+"-地点:" +visit_address
        account_sid = "ACf0f816e3f66d37f0744743b47392ef83"
        auth_token  = "5d59d51a116822ee3831ba9ac89b7eae"
        #send_sms(account_sid,auth_token,from_num,to_num,msg)	
        visit_browser = request.META.get('HTTP_USER_AGENT','unknown')
        visit_page = 'index'
        visit_ip = get_ip(request)
        visit_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        visit = Visit()
        visit.visit_browser = visit_browser
        visit.visit_page = visit_page
        visit.visit_ip = visit_ip 
        visit.visit_time = visit_time
        visit.visit_address = visit_address
        visit.visit_msg = msg
        visit.save()
        visit_count = Visit.objects.count() 
        return render(request,"index.html",{
            'img':img,
            'title':title,
            'img_txt':img_txt,
            'content':content,
            'person':person,
            'netnew':netnew,
            'visit_count':visit_count
        })

class PortfolioView(View):
    def get(self,request):
        title = Title.objects.all()
        div_img = Portfolie.objects.all()
        return render(request,"portfolio.html",{
            'title':title,
            'div_img':div_img,
        })
