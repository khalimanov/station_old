# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_auto_20160127_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='sensor_id',
            field=models.IntegerField(),
        ),
    ]
