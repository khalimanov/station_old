# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='sensor_id',
            field=models.IntegerField(default=0),
        ),
    ]