# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
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
from ORM.tag import Tag
from ORM.relations import Relationships
from ORM.sessions import SessionsManager
# Create your views here.
sess=SessionsManager()
con=Connector()
cat=Category()
tag=Tag()
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
                'tags': req.POST['tags'].strip(),
                'user_id': uid[0]['user_id'],
                'vidcatlist':req.POST.getlist('box')
            }


            vid.insert(data)
            res=vid.get_vid_id(data)
            video_id = res[0]['video_id']
            print(video_id)
            for catid in data['vidcatlist']:
                con.modify("""
                    INSERT INTO Vid_Cat(video_id,cat_id)
                    VALUES(%s,%s);
                """,video_id,int(catid))

            tag.insertTags(data['tags'],video_id)
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

def getChannel(req,chid):
    showdel=False
    uid=sess.checkSession(req)
    pllist=con.query("""SELECT * FROM Playlist WHERE channel_id=%s;""",chid)
    ch=con.query("""SELECT * FROM Channel WHERE channel_id=%s;""",chid)
    if len(ch)!=0:
        if ch[0]['user_id']==uid[0]['user_id']:
            showdel=True
        return render(req,'Frontend/channelpage.html',{'pllist':pllist,'ch':ch,'showdel':showdel})
    else:
        return HttpResponse("<h4>Page not found.</h4>")

def getPlaylist(req,plid):
    showdel=False
    uid=sess.checkSession(req)
    pl=con.query("""SELECT Playlist.*,Channel.user_id 
        FROM Playlist,Channel 
        WHERE Playlist.channel_id=Channel.channel_id AND playlist_id=%s;""",plid)
    vidlist=con.query("""SELECT Video.video_id,Video.title 
            FROM Playlist NATURAL JOIN Pl_Vid NATURAL JOIN Video
            WHERE Playlist.playlist_id=%s;""",plid) 
    if len(pl)!=0:
        if uid!=None:
            if pl[0]['user_id']==uid[0]['user_id']:
                showdel=True
        if len(vidlist)==0:
            return render(req,'Frontend/playlistpage.html',{'msg':"No Videos",'pl':pl,'showdel':showdel})
        else:
            return render(req,'Frontend/playlistpage.html',{'vidlist':vidlist,'pl':pl,'showdel':showdel})
    else:
        return HttpResponse("<h4>Page not found.</h4>")


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
    video = con.query("SELECT * FROM Video NATURAL JOIN User_Profile WHERE video_id=%s",int(video_id))
    comm = con.query("SELECT * FROM  User_Profile NATURAL JOIN Comment where Comment.video_id = %s", video[0]['video_id'])
    if req.method=='GET':
        var = {
            'video' : video[0],
            'comments' : comm,
            'liked' : vid.get_like(video[0]['video_id'])
        }
        return render(req,'Frontend/video.html',var)

def createComment(req,video_id):
    if req.method=='POST':
        vid = con.query("SELECT * FROM Video NATURAL JOIN User_Profile WHERE video_id=%s",int(video_id))
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

def likes(req,video_id):
    uid=sess.checkSession(req)
    if uid!=None :
        if req.method=='GET':
            pass
        elif req.method=='POST':
            if 'like' in req.POST :
                con.modify("""
                    INSERT INTO `Like`(video_id,user_id) VALUES (%s,%s)
                """,int(video_id),int(uid[0]['user_id']))
            elif 'unlike' in req.POST :
                con.modify("""
                    DELETE FROM `Like` WHERE user_id = %s
                """,int(uid[0]['user_id']))
            return redirect('viewVideo',video_id)
    else :
        return redirect('auth:signin')

def addtoplaylist(req,vid):
    uid=sess.checkSession(req)
    if uid!=None :
        if req.method=='GET':
            data=con.query("""
                SELECT channel_id,name AS chname FROM Channel
                WHERE user_id=%s ORDER BY channel_id;            
            """,uid[0]['user_id'])
            for item in data:
                item['playlists']=con.query("""
                    SELECT playlist_id,name AS plname FROM Playlist
                    WHERE channel_id=%s;
                """,item['channel_id'])
            return render(req,'Frontend/addtoplaylist.html',{'data':data,'vid':vid})
        elif req.method=='POST':
            plids=req.POST.getlist('box')
            for item in plids:
                con.modify("""
                    INSERT INTO Pl_Vid
                    VALUES(%s,%s);
                """,vid,int(item))
            return redirect('viewVideo',vid)
    else :
        return redirect('auth:signin')

def removeVidPl(req,plid,vid):
    uid=sess.checkSession(req)
    pluser=con.query("""SELECT user_id FROM Playlist,Channel 
            WHERE Playlist.channel_id=Channel.channel_id 
            AND playlist_id=%s;""",plid)
    if uid!=None:
        if uid[0]['user_id']==pluser[0]['user_id']:
            con.modify("""DELETE FROM Pl_Vid 
                WHERE video_id=%s AND playlist_id=%s;
                """,vid,plid)
        return redirect('getPlaylist',plid)
    else :
        return redirect('auth:signin')

def deletePlaylist(req,plid):
    uid=sess.checkSession(req)
    pluser=con.query("""SELECT user_id FROM Playlist,Channel 
            WHERE Playlist.channel_id=Channel.channel_id 
            AND playlist_id=%s;""",plid)
    if uid!=None:
        if uid[0]['user_id']==pluser[0]['user_id']:
            con.modify("""DELETE FROM Playlist
                WHERE playlist_id=%s;
                """,plid)
        return redirect('userProfile',uid[0]['user_id'])
    else :
        return redirect('auth:signin')

def deleteChannel(req,chid):
    uid=sess.checkSession(req)
    ch=con.query("""SELECT * FROM Channel 
            WHERE channel_id=%s;""",chid)
    if uid!=None:
        if uid[0]['user_id']==ch[0]['user_id']:
            con.modify("""DELETE FROM Channel
                WHERE channel_id=%s;
                """,chid)
            return redirect('userProfile',uid[0]['user_id'])
        else:
            return redirect('getChannel',chid)
    else :
        return redirect('auth:signin')

def getUserDetails(req,usr):
    userdata = (con.query("""
      SELECT * FROM User_Profile WHERE user_id = %s
    """,usr))[0]
    videosdata = (con.query("""
      SELECT * FROM Video WHERE user_id = %s
    """,usr))
    channelsdata = (con.query("""
      SELECT * FROM Channel  WHERE user_id = %s
    """,usr))
    print(videosdata)
    return render(req,'Frontend/user.html',{
        "user":userdata,
        "channels":channelsdata,
        "videos":videosdata,
    })
