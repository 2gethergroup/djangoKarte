from django.contrib.gis import admin
from .models import WeatherStation

#Karta čiji je osnovi lejer OSGeo mapu na nivou 0
admin.site.register(WeatherStation, admin.GeoModelAdmin)