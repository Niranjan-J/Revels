from django.conf.urls import url,include

urlpatterns = [
    url(r'^',include('Frontend.urls')),
    url(r'^auth/',include('Auth.urls')),
]
