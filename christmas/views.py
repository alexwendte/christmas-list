from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *

# Create your views here.
def generic(request):
    return HttpResponse("Hello")

class GroupCreateView(CreateView):
    
    model = Group
    fields = ['name']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('view_group')


class ListListView(ListView):
    


class GroupUpdateView(UpdateView):
    pass


class ListCreateView(CreateView):
    pass


class ListUpdateView(CreateView):
    pass