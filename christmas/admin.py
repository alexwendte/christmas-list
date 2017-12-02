from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Group)
admin.site.register(List)
admin.site.register(Item)
admin.site.register(Profile)