# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-03 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(default='PFxblEp', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=400)),
                ('link', models.CharField(max_length=400)),
                ('picture_link', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('parent_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='christmas.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('google_user_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='list',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_list', to='christmas.Profile'),
        ),
        migrations.AddField(
            model_name='item',
            name='parent_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='christmas.List'),
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(related_name='parent_group', to='christmas.Profile'),
        ),
    ]
