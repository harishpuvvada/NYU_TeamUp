from django.conf.urls import url

from . import views

app_name = 'teamupapp'
urlpatterns = [
    url(r'^$', views.LandingView.as_view(), name='index'),
    url(r'^(?P<userId>[a-zA-Z0-9]+)/myproj/$', views.myProjList, name='myProjList'),
    url(r'^(?P<userId>[a-zA-Z0-9]+)/myproj/$', views.myApplications, name='myApplications'),
    url(r'^(?P<category>[a-zA-Z]+)/list/$', views.projList, name='projList'),
    url(r'^(?P<projectId>[a-zA-Z0-9]+)/detail/$', views.projDetail, name='projDetail'),
]