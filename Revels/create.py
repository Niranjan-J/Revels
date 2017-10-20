from ORM.video import Video
from ORM.category import Category
from ORM.user import User
from ORM.channel import Channel
from ORM.tag import Tag
from ORM.playlist import Playlist
from ORM.comment import Comment
from ORM.profile import Profile
from ORM.sessions import SessionsManager
import os
import environ

if __name__=="__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Revels.settings")

    cat=Category()
    cat.createTable()

    user=User()
    user.createTable()

    vid=Video()
    vid.createTable()

    ch=Channel()
    ch.createTable()

    tg=Tag()
    tg.createTable()

    pl=Playlist()
    pl.createTable()

    com=Comment()
    com.createTable()

    prof=Profile()
    prof.createTable()

    sess=SessionsManager()
    sess.createTable()
