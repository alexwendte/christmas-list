from django.db import models

# Create your models here.

class Group(models.Model):
    
    lists = models.ManyToManyField('List')
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=15)
    people = models.ManyToManyField('Profile')


class List(models.Model):
    
    items = models.ManyToManyField('Item')
    name = models.CharField(max_length=20)
    profile = models.ForeignKey('Profile')
    # decoration = something


class Item(models.Model):
    
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=400)
    link = models.CharField(max_length=400)
    picture_link = models.CharField(max_length=400)
    # claimed_by = something


class Profile(models.Model):
    
    name = models.CharField(max_length=50)
    google_user_id = models.CharField(max_length=100)