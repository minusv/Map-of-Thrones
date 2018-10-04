"""
Atlas URL Configuration
"""

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home, name = 'home'),
    url(r'^(?P<pk>\d+)$',views.visit_kingdom, name = 'kingdom')
]