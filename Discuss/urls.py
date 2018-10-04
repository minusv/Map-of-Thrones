"""
Discuss URL Configuration
"""

from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout

urlpatterns=[
    url(r'^register/', views.register_user, name='register'),
    url(r'^login/', views.login_user, name='login'),
    url(r'^logout/', logout, {'next_page': '/'}),
    url(r'^discuss/', views.discuss, name='discuss'),
    url(r'^post/', views.add_post, name='post'),
]