# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 15:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='some_more_text',
            field=models.CharField(default=datetime.datetime(2016, 2, 26, 15, 20, 23, 718319, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
