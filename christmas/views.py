from django.shortcuts import render, HttpResponse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from .models import *

# Create your views here.
def generic(request):
    return HttpResponse("Hello")

class HomepageView(TemplateView):

    template_name = 'christmas/index.html'


class GroupCreateView(CreateView):
    
    model = Group
    fields = ['name']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('index')


class InviteView(FormView):
    pass

class GroupUpdateView(UpdateView):
    
    model = Group
    fields = ['name']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_object_or_404(Group, address=self.kwargs['group_id'])

    def get_context_data(self, **kwargs):
        context = super(GroupUpdateView, self).get_context_data(**kwargs)
        context['address'] = self.kwargs['group_id']
        context['object_list'] = get_object_or_404(Group, address=self.kwargs['group_id'])
        return context


class ListCreateView(CreateView):
    
    model = List
    fields = ['title', 'description', 'link']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('index')


class ListUpdateView(CreateView):
    
    model = Group
    fields = ['name']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_object_or_404(Group, address=self.kwargs['group_id'])

    def get_context_data(self, **kwargs):
        context = super(GroupUpdateView, self).get_context_data(**kwargs)
        context['address'] = self.kwargs['group_id']
        context['object_list'] = get_object_or_404(Group, address=self.kwargs['group_id'])
        return context