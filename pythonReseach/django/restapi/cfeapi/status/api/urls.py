from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from .views import (
        StatusListSearchAPIView,
        StatusAPIView, 
        StatusCreateAPIView,
        StatusDetailAPIView,
    )

urlpatterns = [
    #path('', StatusListSearchAPIView.as_view()),
    path('', StatusAPIView.as_view()),
    path('create/', StatusCreateAPIView.as_view()),
    url(r'^(?P<id>.*)/$', StatusDetailAPIView.as_view()),
    # path('(P<id>.*)/update/', StatusUpdateAPIView.as_view()),
    # path('(P<id>.*)/delete/', StatusDeleteAPIView.as_view()),
]


#Start with
# /api/status/ -> List
# /api/status/create -> Create
# /api/status/12/ -> Detail
# /api/status/12/update -> Update
# /api/status/12/delete/ -> Delete


# End with
# /api/status/ -> List -> CRUD
# /api/status/1/ -> Detail -> CRUD

# Final
# /api/status/ -> CRUD & LS
