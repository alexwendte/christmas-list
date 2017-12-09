from django.db import models
from django.urls import reverse_lazy

from .helpers import random_alpha_numeric


# Create your models here.
class Group(models.Model):
    
    name = models.CharField(max_length=20, unique=True, blank=False)
    address = models.CharField(max_length=15, default=random_alpha_numeric)
    # users = models.ManyToManyField('Profile', related_name='parent_group')

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy('view_group', kwargs={'group_id':self.address})


class List(models.Model):
    
    name = models.CharField(max_length=20)
    # profile = models.ForeignKey('Profile', related_name='user_list')
    parent_group = models.ForeignKey('Group')

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy('view_list', kwargs={'list_id':self.id, 'group_id':self.parent_group.address})


class Item(models.Model):
    
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=400)
    link = models.CharField(max_length=400)
    picture_link = models.CharField(max_length=400)
    parent_list = models.ForeignKey('List')

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        context = {'item_id':self.id, 'list_id':self.parent_list.id, 'group_id':self.parent_list.parent_group.address}
        return reverse_lazy('view_item', kwargs=context)


class Profile(models.Model):
    
    name = models.CharField(max_length=50)
    google_user_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)