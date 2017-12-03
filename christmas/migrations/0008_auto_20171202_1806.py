# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 00:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('christmas', '0007_auto_20171202_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='parent',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='christmas.List'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='address',
            field=models.CharField(default='GwtU4hh', max_length=15),
        ),
    ]
