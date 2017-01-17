from django.conf.urls import include, url
from django.contrib import admin

from search.views import home
from search.views import search


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^search/(?P<query>.*)$', search, name='search'),
]
