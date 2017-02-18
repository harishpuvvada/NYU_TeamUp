from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^teamupapp/', include('teamupapp.urls')),
    url(r'^admin/', admin.site.urls),
]