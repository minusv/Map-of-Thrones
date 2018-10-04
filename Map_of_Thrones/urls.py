"""
Map_of_Thrones URL Configuration
"""

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('Atlas.urls')),
    url(r'^', include('Discuss.urls')),
]