from django.conf.urls import url,include
from . import views

urlpatterns=[
    url(r'^videos$',views.index,name="index"), 
    url(r'^(?P<catname>[^/]+)/videos$',views.catvideo,name="catvideo"),
]
