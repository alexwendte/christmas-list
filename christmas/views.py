from django.shortcuts import render, HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *

# Create your views here.
def generic(request):
    return HttpResponse("Hello")

class GroupCreateView(CreateView):
    
    model = Group
    fields = ['name', 'lists']


class ListListView(ListView):
    pass


class GroupUpdateView(UpdateView):
    pass


class ListCreateView(CreateView):
    pass


class ListUpdateView(CreateView):
    pass