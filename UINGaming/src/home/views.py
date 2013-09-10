#!/usr/bin/env python
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from src.authentication.models import User

def HomeView(request):
    if request.method == 'GET':
        information = {}
        information['login'] = True
        username = request.get_signed_cookie('user_id','')
        information['user']  = User.getByUsername(username)
        if information['user'] is None:
            information['login'] = False
        return render_to_response('index.html',information,RequestContext(request))
    else:
        pass # TODO POST METHOD

def SlidesAPI(request):
    pass

def FeaturesAPI(request):
    pass