from django import forms
from .models import *

class InviteForm(forms.Form):

    pass


class ListCreateForm(forms.ModelForm):
    
    class Meta():
        model = List
        fields = ['name']
        # widgets = {
        #     'group_address': forms.HiddenInput(),
        # }


class ItemCreateForm(forms.ModelForm):
    
    class Meta():
        model = Item
        fields = ['title', 'description', 'link']
        # widgets = {
        #     'group_address': forms.HiddenInput(),
        #     'parent_id': forms.HiddenInput(),
        # }