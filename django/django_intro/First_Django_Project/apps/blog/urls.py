from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^blogs$', views.index), #this is your html file redirect
    url(r'^blogs/new$', views.new),
    url(r'^blogs/create$', views.create),
    url(r'^blogs/(?P<number>\d+)$', views.show),
    url(r'^blogs/(?P<number>\d+)/edit$', views.edit),
    url(r'^blogs/(?P<number>\d+)/delete$', views.destroy),
]