'''
Created on 2013-6-28

@author: fenglvming
'''
from django.contrib import admin
from DjangoTest.users.models import Users
from DjangoTest.users.models import WeiboSettings

class UsersAdmin(admin.ModelAdmin):
    fields = ('weiboid','weibousername','weibodomain','weibogender','weiboavatarlarge')
    list_display = ('weiboid','weibousername','weibodomain','weibogender','weiboavatarlarge')
    search_fields = ['weibousername']

class WeiboSettingsAdmin(admin.ModelAdmin):
    fields = ('appkey','appsecret')
    list_display = ('appkey','appsecret')

admin.site.register(Users, UsersAdmin)
admin.site.register(WeiboSettings,WeiboSettingsAdmin)
