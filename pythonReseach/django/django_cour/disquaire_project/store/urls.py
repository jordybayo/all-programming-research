from django.conf.urls import url

from . import views  #import views so we can use them in urls


urlpatterns = [
	url(r'^$', views.listing, name="listing"), #"/store" will call the mdethod "index" in "views.py"
	url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"), #/store/2
	url(r'^search/', views.search, name="search"),
]

app_name = 'store'