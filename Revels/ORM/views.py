from django.shortcuts import render
from django.http import JsonResponse
from ORM.dbconnect import Connector;
from ORM.video import Video;

def blah(request):
    conn = Connector()
    vid = Video()
    vid.create({"title":"hello","descr":"hello","url":"hello","img":"hello","user_id":1})
    vid.insert()
    return JsonResponse({"token": "dgfsdg"})
