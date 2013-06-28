'''
Created on 2013-6-28

@author: fenglvming
'''
from django.contrib import admin
from DjangoTest.users.models import Users

class UsersAdmin(admin.ModelAdmin):
    fields = ('username', 'email','password')
    list_display = ('username', 'email','password')
admin.site.register(Users, UsersAdmin)