from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.partner_list, name='partner_list'),
    url(r'^partners/(?P<pk>[0-9]+)/$', views.partner_detail, name='partner_detail'),
    url(r'^partners/(?P<pk>[0-9]+)/edit/$', views.partner_edit, name='partner_edit'),
    url(r'^add/$', views.partner_add, name='partner_add'),
]
