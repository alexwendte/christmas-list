# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('christmas', '0008_auto_20171202_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='profile',
        ),
        migrations.AlterField(
            model_name='group',
            name='address',
            field=models.CharField(default='3USz9LM', max_length=15),
        ),
    ]