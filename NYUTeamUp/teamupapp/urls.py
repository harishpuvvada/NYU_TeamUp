from django.conf.urls import url

from . import views

app_name = 'teamupapp'
urlpatterns = [
    url(r'^$', views.LandingView.as_view(), name='index'),
    url(r'^(?P<ct>[0-9]+)/$', views.ProjListView.as_view(), name='list'),
]