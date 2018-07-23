from django.conf.urls import url,include
from django.contrib import admin
# from .views import StatusListSearchApi,StatusCreateApiView,StatusDetailApiView,StatusUpdateApiView,StatusDeleteApiView
from .views import StatusListSearchApi
# StatusCreateApiView,StatusDetailApiView,StatusUpdateApiView,StatusDeleteApiView

urlpatterns = [
        # url(r'^$/', StatusListSearchApi.as_view()),
        url(r'^list/', StatusListSearchApi.as_view()),
        # url(r'^(?P<id>\d+)/$',RetrieveUpdateDestroyAPIView.as_view()),

        # url(r'^create/$',StatusCreateApiView.as_view()),
        # url(r'^(?P<id>\d+)/', StatusDetailApiView.as_view()),
        # url(r'^(?P<id>\d+)/update/', StatusUpdateApiView.as_view()),
        # url(r'^(?P<id>\d+)/delete/', StatusDeleteApiView.as_view()),

]
