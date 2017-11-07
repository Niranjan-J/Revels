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
import os
import environ

if __name__=="__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Revels.settings")

    cat=Category()
    cat.createTable()
    cat.createTriggers()

    user=User()
    user.createTable()
    user.createTriggers()

    vid=Video()
    vid.createTable()
    vid.createTriggers()

    ch=Channel()
    ch.createTable()
    ch.createTriggers()

    tg=Tag()
    tg.createTable()
    tg.createTriggers()
    tg.create_Procs()

    pl=Playlist()
    pl.createTable()
    pl.createTriggers()

    com=Comment()
    com.createTable()
    com.createTriggers()

    prof=Profile()
    prof.createTable()
    prof.createTriggers()

    sess=SessionsManager()
    sess.createTable()
    sess.createTriggers()

    rel = Relationships()
    rel.create_UsersProfile()
    rel.create_Like()
    rel.create_Pl_Vid()
    rel.create_Subscription()
    rel.create_Vid_Cat()
