'''
Created on 2013-6-28

@author: fenglvming
'''
from django.db import models
from django.utils.html import format_html

class Users(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return 'your name is:%s  email is:%s' % (self.username,self.email)

