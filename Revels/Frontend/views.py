# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from ORM.dbconnect import Connector
from ORM.video import Video
from ORM.category import Category
from ORM.user import User
from ORM.channel import Channel
from ORM.tag import Tag
from ORM.playlist import Playlist
from ORM.comment import Comment
from ORM.profile import Profile
from ORM.relations import Relationships
from ORM.sessions import SessionsManager
# Create your views here.
sess=SessionsManager()
con=Connector()
cat=Category()
vid=Video()

def index(req):
    return render(req,'Frontend/index.html',{"category":cat.getall()})

def catvideo(req,catname):   
    data=cat.get_CatVideos(catname)
    return render(req,'Frontend/category.html',{"data": data})

def upload(req):
    uid=sess.checkSession(req)
    catlist=cat.getall()
    if uid!=None :
        if req.method=='GET':
            return render(req,'Frontend/upload.html',{'category':catlist})
        elif req.method=='POST':
            data={
                'title': req.POST['title'].strip(), 
                'descr':req.POST['descr'].strip(), 
                'url': req.POST['url'].strip(), 
                'user_id': uid[0]['user_id'],
                'vidcatlist':req.POST.getlist('box')
            }
            vid.insert(data)
            id=vid.get_vid_id(data)
            print(id)
            for catid in data['vidcatlist']:
                con.modify("""
                    INSERT INTO Vid_Cat(video_id,cat_id)
                    VALUES(%s,%s);
                """,id[0]['video_id'],int(catid))
            return render(req,'Frontend/upload.html',{'category':catlist,'msg':"Uploaded Sucessfully"})
    else:
        return redirect('/auth/signin')

