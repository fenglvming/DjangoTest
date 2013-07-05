from django.conf.urls import patterns, include, url
from django.contrib import admin  
from weibo import *
from DjangoTest.users.models import *
from DjangoTest.users.views import *


_APP_ID = ''
_APP_SECRET = ''
_APP_CALLBACK = ''

admin.autodiscover()

urlpatterns = patterns('',  
    (r'^admin/', include(admin.site.urls)),
    (r'^auth/login',weibo_auth_login),
    (r'^$',weibo_index),
    (r'^auth/callback',weibo_auth_callback)
)




def _init_weibo_settings():
    global _APP_ID, _APP_SECRET,_APP_CALLBACK
    currentWeiboSettings = WeiboSettings.objects.order_by('addtime')
    if len(currentWeiboSettings):
        _APP_ID = currentWeiboSettings[0].appkey
        _APP_SECRET = currentWeiboSettings[0].appsecret
        _APP_CALLBACK = currentWeiboSettings[0].callbackurl
    else:
        _APP_ID = "1737674077"
        _APP_SECRET = "14b90383cea503e4840335bfd71eacf6"
        _APP_CALLBACK = "http://todolists.sinaapp.com/auth/callback"

def _create_client():
    return APIClient(_APP_ID, _APP_SECRET, _APP_CALLBACK)

_init_weibo_settings()