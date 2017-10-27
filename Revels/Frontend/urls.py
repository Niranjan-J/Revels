from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^videos/$',views.index,name="index"),
    url(r'^videos/(?P<catname>[^/]+)/$',views.catvideo,name="catvideo"),
    url(r'^upload/$',views.upload,name="upload"),
    url(r'^channels/$',views.showChannels,name='showChannels'),
    url(r'^(?P<chname>[^/]+)/$',views.getChannel,name='getChannel'),
    url(r'^create_channel/$',views.createChannel, name='createChannel'),
    url(r'^(?P<chid>[^/]+)/create_playlist/$',views.createPlaylist,name='createPlaylist')
]
