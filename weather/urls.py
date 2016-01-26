from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /weather/
    url(r'^$', views.index, name='index'),
    # ex: /weather/1/
    url(r'^(?P<sensor_id>[0-9]+)/$', views.sensorname, name='sensorname'),
    # ex: /weather/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /weather/5/addvalue/
    url(r'^(?P<question_id>[0-9]+)/addvalue/$', views.addvalue, name='addvalue'),
]