from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^videos$',views.index,name="index"),
    url(r'^videos/(?P<catname>[^/]+)$',views.catvideo,name="catvideo"),
]
