from django.conf.urls import url
from django.shortcuts import render

from .views import *

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='index'),
    url(r'^create/$', GroupCreateView.as_view(), name='create_group'),
    url(r'^(?P<group_id>[0-9A-Za-z]+)/$', GroupUpdateView.as_view(), name='view_group'),
    url(r'^(?P<group_id>[0-9A-Za-z]+)/invite/$', InviteView.as_view(), name='invite'),
    url(r'^(?P<group_id>[0-9A-Za-z]+)/create/$', ListCreateView.as_view(), name='create_list'),
    url(r'^(?P<group_id>[0-9A-Za-z]+)/(?P<list_id>[0-9]+)/$', ListUpdateView.as_view(), name='view_list'),
    # url(r'^(?P<group_id>[0-9A-Za-z]+)/(?P<list_id>[0-9]+)/$', ListUpdateView.as_view(), name='view_list'),
]