from django.db import models

# Create your models here.

class Group(models.Model):
    
    lists = models.ManyToManyField()
    # name = models.CharField()
    pass


class List(models.Model):
    pass


class Item(models.Model):
    pass