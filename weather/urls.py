from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /weather/
    url(r'^$', views.index, name='index'),
    # ex: /weather/1/
    url(r'^(?P<sensor_id>[0-9]+)/$', views.sensorname, name='sensorname'),
    # ex: /weather/results/
    url(r'^results/$', views.results, name='results'),
    # ex: /weather/addvalue/   
    url(r'^addvalue/$', views.addvalue, name='addvalue'),
]
