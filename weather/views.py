from django.shortcuts import render

from django.http import HttpResponse

from .models import Sensor


def index(request):
    sensor_list = Sensor.objects.all()
    output = ', '.join([p.sensor_name for p in sensor_list])
    return HttpResponse(output)

def sensorname(request, sensor_id):
    return HttpResponse("You're looking at sensor %s." % sensor_id)

def results(request, sensor_id):
    response = "You're looking at the results of sensor %s."
    return HttpResponse(response % sensor_id)

def addvalue(request, sensor_id):
    return HttpResponse("You're addind value at sensor %s." % sensor_id)