# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ORM.video import Video
# Create your views here.

def index(req):
    vid = Video()
    return render(req,'index.html',{ 'data': vid.getallvideos() })