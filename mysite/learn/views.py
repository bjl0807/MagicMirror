from django.shortcuts import render

# Create your views here.
#coding:utf-8
from django.shortcuts import render
import time
from django_websocket import require_websocket
from django_websocket import accept_websocket

def GetNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def home(request):
    string = u"lla";
    time = GetNowTime();
    return render(request, 'home.html', {'time': time});
