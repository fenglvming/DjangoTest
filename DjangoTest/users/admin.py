'''
Created on 2013-6-28

@author: fenglvming
'''
from django.contrib import admin
from DjangoTest.users.models import Users

#Ϊ���ú�̨����Ľ����ܹ��������Ƕ���Ķ���Ĺ���.������ÿ��app�¼�admin.py
class UsersAdmin(admin.ModelAdmin):
    fields = ('username', 'email','password')
    #���ô�ͳ���б�ķ�ʽչ������,Ҫչ����Щ���г���Щ����.
    list_display = ('username', 'email','password')
admin.site.register(Users, UsersAdmin)