# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Sensor, Temperature, Humidity
from django.views.decorators.csrf import csrf_exempt


def index(request):
    sensor_list = Sensor.objects.all()
    context = {'sensor_list': sensor_list}
    return render(request, 'weather/index.html', context)


def sensorname(request, sensor_id):
    return HttpResponse("You're looking at sensor {}.".format(sensor_id))


def results(request):
    values_list = Temperature.objects.all()
    context = {'values_list': values_list}
    return render(request, 'weather/temperature.html', context)


@csrf_exempt
def addvalue(request):
    if request.method != 'POST':
        return HttpResponse('request need to be POST')
    sensor_id = request.POST.get("sensor_id", 0)
    temp = request.POST.get('temp', 0)
    hum = request.POST.get('hum', 0)
    if sensor_id == 0 or hum == 0:
        return HttpResponse('Bad info')
    sensor = Sensor.objects.get(sensor_id_const=sensor_id)
    new_temp = Temperature()
    new_temp.sensor = sensor
    new_temp.value = temp
    new_temp.save()
    new_hum = Humidity()
    new_hum.sensor = sensor
    new_hum.value = hum
    new_hum.save()
    return HttpResponse('200 OK')
