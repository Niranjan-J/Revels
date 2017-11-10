from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^videos/(?P<video_id>[^/]+)/$',views.viewVideo,name="viewVideo"),
    url(r'^categories/(?P<catid>[^/]+)/$',views.catvideo,name="catvideo"),
    url(r'^upload/$',views.upload,name="upload"),
    url(r'^channel/(?P<chid>[^/]+)/$',views.getChannel,name='getChannel'),
    url(r'^playlist/(?P<plid>[^/]+)/$',views.getPlaylist,name='getPlaylist'),
    url(r'^create_channel/$',views.createChannel, name='createChannel'),
    url(r'^create_playlist/(?P<chid>[^/]+)$',views.createPlaylist,name='createPlaylist'),
    url(r'^create_comment/(?P<video_id>[^/]+)/$',views.createComment,name="create_comment"),
    url(r'^likes/(?P<video_id>[^/]+)/$',views.likes,name="likes"),
    url(r'^addpl/(?P<vid>[^/]+)/$',views.addtoplaylist,name='addtoplaylist'),
    url(r'^users/(?P<usr>[^/]+)/$',views.getUserDetails,name='userProfile'),
    url(r'^removepl/(?P<plid>[^/]+)/(?P<vid>[^/]+)/$',views.removeVidPl,name='removeVidPl'),
    url(r'^deletepl/(?P<plid>[^/]+)/$',views.deletePlaylist,name='deletePlaylist'),
    url(r'^deletech/(?P<chid>[^/]+)/$',views.deleteChannel,name='deleteChannel'),
    url(r'^search/$',views.search,name="search"),
    url(r'^search/(?P<cat>[^/]+)/(?P<query>[^/]+)/$',views.searchResult,name="seastatic in djangorchResult"),
    url(r'^subscribe/(?P<chid>[^/]+)/$',views.subscribe,name='subscribe'),
]

