from django.conf.urls import include, url
from django.contrib import admin

from partners import views

urlpatterns = [
    url(r'^_ope_/', include(admin.site.urls)),
    url(r'', include('home.urls')),

    url(r'^partners/', include('partners.urls')),
    url(r'^places/', include('places.urls')),
]
