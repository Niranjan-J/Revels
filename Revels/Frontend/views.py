# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
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

con=Connector()

def index(req):
    cat=Category()
    return render(req,'Frontend/index.html',{"category":cat.getall()})

def catvideo(req,catname):
    data=con.query("""
        SELECT Video.*,Category.text FROM Video,Category,Vid_Cat 
        WHERE Video.video_id=Vid_Cat.Video_id 
        AND Vid_Cat. cat_id=Category.cat_id AND Category.text=%s
        """,catname)
    return render(req,'Frontend/category.html',{"data": data})
