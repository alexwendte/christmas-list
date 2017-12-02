from django.db import models
from .helpers import random_alpha_numeric

# Create your models here.

class Group(models.Model):
    
    lists = models.ManyToManyField('List')
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=15, default=random_alpha_numeric(7))
    people = models.ManyToManyField('Profile')

    def __str__(self):
        return str(self.name)


class List(models.Model):
    
    items = models.ManyToManyField('Item')
    name = models.CharField(max_length=20)
    profile = models.ForeignKey('Profile')
    # decoration = something

    def __str__(self):
        return str(self.name)


class Item(models.Model):
    
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=400)
    link = models.CharField(max_length=400)
    picture_link = models.CharField(max_length=400)

    def __str__(self):
        return str(self.title)


class Profile(models.Model):
    
    name = models.CharField(max_length=50)
    google_user_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)