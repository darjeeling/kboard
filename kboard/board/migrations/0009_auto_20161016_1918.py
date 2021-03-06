# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-16 19:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_board_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 16, 19, 18, 19, 794242, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterIndexTogether(
            name='post',
            index_together=set([]),
        ),
    ]
