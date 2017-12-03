from django.shortcuts import render, HttpResponse, get_object_or_404

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from .models import *

# Create your views here.
class HomepageView(TemplateView):

    template_name = 'christmas/index.html'


class GroupCreateView(CreateView):
    
    model = Group
    fields = ['name']
    template_name_suffix = '_create_form'


class InviteView(FormView):
    pass


class GroupUpdateView(UpdateView):
    
    model = Group
    fields = ['name']
    template_name_suffix = '_update_form'

    def get_object(self, queryset=None):
        return get_object_or_404(Group, address=self.kwargs['group_id'])

    def get_context_data(self, **kwargs):
        context = super(GroupUpdateView, self).get_context_data(**kwargs)
        context['address'] = self.kwargs['group_id']
        context['object_list'] = get_object_or_404(Group, address=self.kwargs['group_id'])
        return context


class ListCreateView(CreateView):
    
    model = List
    fields = ['name', 'group_address']
    template_name_suffix = '_create_form'

    def get_initial(self, **kwargs):
        newInitial = self.initial
        newInitial['group_address'] = self.kwargs['group_id']
        return newInitial


class ListUpdateView(UpdateView):
    
    model = List
    fields = ['name']
    template_name_suffix = '_update_form'

    def get_object(self, queryset=None):
        return get_object_or_404(List, id=self.kwargs['list_id'])

    def get_context_data(self, **kwargs):
        context = super(ListUpdateView, self).get_context_data(**kwargs)
        context['address'] = self.kwargs['group_id']
        context['object_list'] = list(get_object_or_404(List, id=self.kwargs['list_id']).items)
        return context