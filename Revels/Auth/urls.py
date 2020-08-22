from django.conf.urls import url,include
from . import views

app_name = 'auth'
urlpatterns = [
    url(r'^signup',views.SignUp.as_view(),name='signup'),
    url(r'^signin',views.SignIn.as_view(),name='signin'),
    url(r'^signout',views.SignOut,name='signout'),
    url(r'^profile',views.Profile,name='profile'),
    url(r'^',views.Home.as_view(),name='home'),
]
