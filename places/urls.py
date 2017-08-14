from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.place_list, name='place_list'),
    url(r'^places/(?P<pk>[0-9]+)/$', views.place_detail, name='place_detail'),
    url(r'^places/(?P<pk>[0-9]+)/edit/$', views.place_edit, name='place_edit'),
    url(r'^add/$', views.place_add, name='place_add'),
    url(r'^get/$', views.places_get, name='places_get'),
]
