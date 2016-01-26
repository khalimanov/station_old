from __future__ import unicode_literals

from django.db import models

class Sensor(models.Model):
	sensor_name = models.CharField(max_length=100)

class Temperature(models.Model):
	sensor = models.ForeignKey(Sensor)
	value = models.FloatField()
	date = models.DateTimeField(auto_now=True)