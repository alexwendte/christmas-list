# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-07 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christmas', '0003_auto_20171207_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='users',
        ),
        migrations.AlterField(
            model_name='group',
            name='address',
            field=models.CharField(default='FHY0QlZ', max_length=15),
        ),
    ]
