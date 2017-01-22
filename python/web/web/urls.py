from django.conf.urls import include, url
from django.contrib import admin

from search.views import home
from search.views import search_content
from search.views import search_title


urlpatterns = [
    url(r'^$', home, name='home'),
	url(r'^search/title/(?P<query>.*)$', search_title, name='search-title'),
    url(r'^search/content/(?P<query>.*)$', search_content, name='search-content'),
]
