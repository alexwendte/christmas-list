from django.conf.urls import url
from django.shortcuts import render

from .views import *

urlpatterns = [
    url(r'^$', GroupCreateView.as_view(), name='index'),
]