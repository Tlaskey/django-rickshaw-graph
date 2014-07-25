from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^graph/', include('graph.urls')),
    url(r'^admin/', include(admin.site.urls)),
]