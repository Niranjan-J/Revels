from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^videos/$',views.index,name="index"),
    url(r'^videos/(?P<video_id>[^/]+)/$',views.viewVideo,name="viewVideo"),
    url(r'^categories/(?P<catname>[^/]+)/$',views.catvideo,name="catvideo"),
    url(r'^upload/$',views.upload,name="upload"),
    url(r'^channels/$',views.showChannels,name='showChannels'),
    url(r'^channels/(?P<chname>[^/]+)/$',views.getChannel,name='getChannel'),
    url(r'^create_channel/$',views.createChannel, name='createChannel'),
    url(r'^(?P<chid>[^/]+)/create_playlist/$',views.createPlaylist,name='createPlaylist'),
    url(r'^create_comment/(?P<video_id>[^/]+)/$',views.createComment,name="create_comment"),
    url(r'^likes/(?P<video_id>[^/]+)/$',views.likes,name="likes"),
]
