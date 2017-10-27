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
        return redirect('auth:signin')

def showChannels(req):
    uid=sess.checkSession(req)
    if uid!=None:
        chlist=con.query("SELECT name FROM Channel WHERE user_id=%s",uid[0]['user_id'])
        if len(chlist)==0:
            return render(req,'Frontend/channels.html',{'msg': "You don\'t have any Channels..."})
        else:
            return render(req,'Frontend/channels.html',{'msg':"Your Channels:",'chlist': chlist})
    else:
        return redirect('auth:signin')

def createChannel(req):
    uid=sess.checkSession(req)
    if uid!=None:
        if req.method=='GET':
            return render(req,'Frontend/createchannel.html',{})
        elif req.method=='POST':
            data={
                'name': req.POST['name'].strip(),
                'descr':req.POST['descr'].strip(),
                'defpl':req.POST['defpl'].strip(),
            }
            chid=len(con.query("SELECT channel_id FROM Channel;"))+1
            con.modify("""
                INSERT INTO Channel(name,description,user_id)
                VALUES(%s,%s,%s);
            """,data['name'],data['descr'],uid[0]['user_id'])
            con.modify("""
                INSERT INTO Playlist(name,channel_id)
                VALUES(%s,%s);
            """,data['defpl'],chid)
            return render(req,'Frontend/createchannel.html',{'msg':"Channel Successfully created !!"})
    else:
        return redirect('auth:signin')

def getChannel(req,chname):
    uid=sess.checkSession(req)
    if uid!=None:
        data=con.query("""
            SELECT Playlist.playlist_id,Playlist.name AS plname,Channel.* FROM Channel,Playlist
            WHERE Channel.channel_id=Playlist.channel_id AND
            Channel.name=%s AND Channel.user_id=%s;
        """,chname,uid[0]['user_id'])
        plvideo=[]
        for item in data:
            item['videos']=con.query("SELECT Video.* FROM Video NATURAL JOIN Pl_Vid WHERE playlist_id=%s",item['playlist_id'])
        return render(req,'Frontend/mychannel.html',{'data':data })
    else:
        return redirect('auth:signin')

def createPlaylist(req,chid):
    uid=sess.checkSession(req)
    if uid!=None:
        ch=con.query("SELECT channel_id,name FROM Channel WHERE channel_id=%s",chid)
        if req.method=='GET':
            return render(req,'Frontend/createplaylist.html',{'ch':ch})
        elif req.method=='POST':
            con.modify("""
                INSERT INTO Playlist(name,channel_id)
                VALUES(%s,%s);
            """,req.POST['name'].strip(),ch[0]['channel_id'])
            return render(req,'Frontend/createplaylist.html',{'ch':ch,'msg':"Playlist Successfully created !!"})
    else:
        return redirect('auth:signin')

def viewVideo(req,video_id):

        vid = con.query("SELECT * FROM Video NATURAL JOIN User_Profile WHERE video_id=%s",int(video_id))
        comm = con.query("SELECT * FROM  User_Profile NATURAL JOIN Comment where Comment.video_id = %s", vid[0]['video_id'])

        if req.method=='GET':

            var = {
                'video' : vid[0],
                'comments' : comm,
            }
            return render(req,'Frontend/video.html',var)
        elif req.method=='POST':

            uid=sess.checkSession(req)
            if uid!=None:
                comm = req.POST['comment'].strip()
                con.modify("""
                    INSERT INTO Comment(text, timestamp, video_id, user_id) VALUES (%s,CURRENT_TIMESTAMP(),%s,%s)
                """, comm, vid[0]['video_id'],uid[0]['user_id'])
                comm = con.query("SELECT * FROM  User_Profile NATURAL JOIN Comment where Comment.video_id = %s", vid[0]['video_id'])
                var = {
                    'video' : vid[0],
                    'comments' : comm,
                }
                return render(req,'Frontend/video.html',var)
            else:
                return redirect('auth:signin')
