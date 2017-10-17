from django.shortcuts import render
from django.http import JsonResponse
from ORM.dbconnect import Connector;
from ORM.video import VideoManager;

def blah(request):
    conn = Connector()
    vid = VideoManager()
    vid.insert({"title":"helo","descr":"hello","url":"hello","img":"hello","user_id":1})
    return JsonResponse({"token": "dgfsdg"})
