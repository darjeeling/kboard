# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-22 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_auto_20161016_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
