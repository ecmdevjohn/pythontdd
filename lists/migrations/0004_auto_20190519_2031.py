# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-19 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='text',
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.TextField(default=''),
        ),
    ]
