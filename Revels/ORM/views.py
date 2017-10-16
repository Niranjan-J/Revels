from django.shortcuts import render
from django.http import JsonResponse
from ORM.dbconnect import Connector;
from ORM.video import VideoManager;

def blah(request):
    conn = Connector()
    r = conn.query("show databases")
    vid = VideoManager()
    vid.create_table()
    print(r)
    return JsonResponse({"token": "dgfsdg"})
