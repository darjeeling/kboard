# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
