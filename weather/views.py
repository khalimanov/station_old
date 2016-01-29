# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Sensor


def index(request):
    sensor_list = Sensor.objects.all()
    context = {'sensor_list': sensor_list}
    return render(request, 'weather/index.html', context)


def sensorname(request, sensor_id):
    return HttpResponse("You're looking at sensor {}.".format(sensor_id))


def results(request, sensor_id):
    return HttpResponse("You're looking at the results of sensor {}".format(sensor_id))


def addvalue(request):
    if request.PUT is False:
        return HttpResponse('request need to be PUT')
    return HttpResponse('200 OK')
