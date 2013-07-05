'''
Created on 2013-7-5

@author: fenglvming
'''
import DjangoTest.urls
import time, json, base64, logging, hashlib
from datetime import datetime, tzinfo, timedelta
from django.http import HttpResponseRedirect
from django.http import response
from django import http
from django.http import HttpResponse 
from DjangoTest.users.models import Users
from django.shortcuts import redirect
from weibo import *
from django.template import RequestContext, loader

def weibo_index(request):
    u = _check_cookie(request)
    if u is None:
        return HttpResponseRedirect("/auth/login")
    return weibo_real_index2(request,u)

def weibo_real_index(request,user):
    template = loader.get_template('users/index.html')
    context = RequestContext(request, {
    'username': user.weibousername,
    })
    response = HttpResponse(template.render(context))
    return response

def weibo_real_index2(request,user):
    template = loader.get_template('users/index2.html')
    context = RequestContext(request, {
    'username': user.weibousername,
    })
    return HttpResponse(template.render(context))

def weibo_auth_login(request):
    client = DjangoTest.urls._create_client()
    return HttpResponseRedirect(client.get_authorize_url())

def weibo_auth_callback(request):
    code = request.GET['code']
    try:
        client = DjangoTest.urls._create_client()
        r = client.request_access_token(code)
        access_token, expires_in, uid = r.access_token, r.expires_in, r.uid
        client.set_access_token(access_token, expires_in)
        u = client.users.show.get(uid=uid)
        users = Users.objects.filter(weiboid=u.id)
        user = Users(weibousername=u.screen_name, \
                weiboavatarlarge=u.avatar_large or u.profile_image_url, \
                weibotoken=access_token, \
                weiboexpires=expires_in,\
                weiboid=u.id,\
                weibodomain=u.domain,\
                weibogender=u.gender)
        user.weiboupdatetime = datetime.utcnow()
        response = HttpResponse()
        _make_cookie(response,uid,expires_in)
        if len(users):
            user.id = users[0].id
            user.weiboaddtime = users[0].weiboaddtime
            user.save()
        else:
            user.weiboaddtime = user.weiboupdatetime
            user.save()
    except APIError :
        return HttpResponseRedirect('/error')
    return response
    

_COOKIE = 'todolists'
_SALT = 'whatalovelyday'

def _make_cookie(response,uid,expires_in):
    expires = str(int(expires_in))
    cookie = '%s:%s' % (str(uid), expires)
    '''md5 = hashlib.md5(s).hexdigest()
    cookie = '%s:%s:%s' % (str(uid), expires, md5)'''
    response.set_cookie(_COOKIE,base64.b64encode(cookie).replace('=', '_'),expires,expires,'/','.sinaapp.com')
    '''response.set_cookie(_COOKIE,base64.b64encode(cookie).replace('=', '_'),expires,'/','sinaapp.com')'''
    
def _check_cookie(request):
    try:
        b64cookie = request.COOKIES[_COOKIE]
        cookie = base64.b64decode(b64cookie.replace('_', '='))
        uid,expires = cookie.split(':', 2)
        if int(expires) < time.time():
            return
        L = Users.objects.filter(weiboid=uid)
        if not L:
            return
        u = L[0]
        return u
    except BaseException:
        raise