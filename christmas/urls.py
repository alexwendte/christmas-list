from django.conf.urls import url
from django.shortcuts import render

from . import views

urlpatterns = [
    url(r'^$', views.generic, name='index'),
]