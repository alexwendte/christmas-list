from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    success_url = reverse_lazy('view_group')


class ListView(ListView):
    
    model = List

    def get_queryset(self, **kwargs):
        queryset = List.ojects.filter()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(FarmList, self).get_context_data(**kwargs)
        context['isManager'] = self.request.user.has_perm("mainForm.view_all_data")
        return context


class GroupUpdateView(UpdateView):
    pass


class ListCreateView(CreateView):
    pass


class ListUpdateView(CreateView):
    pass