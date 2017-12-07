from django.shortcuts import render, HttpResponse, get_object_or_404

from django.views.generic.base import View, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from .models import *
from .forms import *

# Create your views here.
class HomepageView(TemplateView):

    template_name = 'christmas/index.html'

class TokenView(View):

    def post(self, request, *args, **kwargs):
        print(request.POST)

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
    fields = ['name']
    template_name_suffix = '_create_form'

    def form_valid(self, form):
         parent_group = get_object_or_404(Group, address=self.kwargs['group_id'])
         form.instance.parent_group = parent_group
         return super(ListCreateView, self).form_valid(form)

    # def get_initial(self, **kwargs):
    #     newInitial = self.initial
    #     newInitial['parent_group'] = get_object_or_404(Group, address=self.kwargs['group_id'])
    #     return newInitial


class ListUpdateView(UpdateView):
    
    model = List
    fields = ['name']
    template_name_suffix = '_update_form'

    def get_object(self, queryset=None):
        return get_object_or_404(List, id=self.kwargs['list_id'])

    def get_context_data(self, **kwargs):
        context = super(ListUpdateView, self).get_context_data(**kwargs)
        context['address'] = self.kwargs['group_id']
        print(type(get_object_or_404(List, id=self.kwargs['list_id']).items))
        # context['object_list'] = 
        return context


class ItemCreateView(CreateView):
    
    model = Item
    form_class = ItemCreateForm
    template_name_suffix = '_create_form'

    def get_initial(self, **kwargs):
        newInitial = self.initial
        newInitial['group_address'] = self.kwargs['group_id']
        newInitial['parent_id'] = self.kwargs['list_id']
        return newInitial


class ItemUpdateView(UpdateView):
    
    model = Item
    fields = ['title', 'description', 'link']
    template_name_suffix = '_update_form'

    def get_object(self, queryset=None):
        return get_object_or_404(Item, id=self.kwargs['item_id'])