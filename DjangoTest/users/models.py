'''
Created on 2013-6-28

@author: fenglvming
'''
from django.db import models
from django.utils.html import format_html

class Users(models.Model):
    weibousername = models.CharField(max_length=50)
    weiboavatarlarge = models.CharField(max_length=500)
    weibotoken = models.CharField(max_length=50)
    weiboexpires = models.FloatField()
    weiboid = models.IntegerField()
    weibodomain = models.CharField(max_length=200)
    weibogender = models.CharField(max_length=20)
    weiboaddtime = models.DateTimeField()
    weiboupdatetime = models.DateTimeField()
    def __str__(self):
        return 'your name is:%s  id is:%s' % (self.weibousername,self.id)

class WeiboSettings(models.Model):
    appkey = models.CharField(max_length = 50)
    appsecret = models.CharField(max_length = 50)
    addtime = models.DateField()
    callbackurl = models.CharField(max_length = 100)
    def __str__(self):
        return 'your weibo appkey is :%s  secret is:%s' % (self.appkey,self.appsecret)

