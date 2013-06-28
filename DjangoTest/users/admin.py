'''
Created on 2013-6-28

@author: fenglvming
'''
from django.contrib import admin
from DjangoTest.users.models import Users

#为了让后台管理的界面能够加入我们定义的对象的管理.所以在每个app下加admin.py
class UsersAdmin(admin.ModelAdmin):
    fields = ('username', 'email','password')
    #采用传统的列表的方式展现数据,要展现那些就列出那些属性.
    list_display = ('username', 'email','password')
admin.site.register(Users, UsersAdmin)