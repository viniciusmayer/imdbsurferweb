# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdbsurfer', '0004_auto_20170624_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviegenre',
            name='index',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
