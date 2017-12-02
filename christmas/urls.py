from django.conf.urls import url
from django.shortcuts import render

from .views import *

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='index'),
    url(r'^$', GroupCreateView.as_view(), name='create_group'),
    url(r'^(?P<group_id>[0-9]+)/', ListView.as_view(), name='view_group'),
]