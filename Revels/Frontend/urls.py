from django.conf.urls import url,include
from . import views

from Auth import views as authViews
urlpatterns=[
    url(r'^videos/',views.index),
    url(r'^auth/',include('Auth.urls')), # Adds urls from Auth.urls 
]
