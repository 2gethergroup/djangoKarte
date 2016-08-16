from django.shortcuts import render
from .models import WeatherStation
from django.http import JsonResponse
# Create your views here.

def metStanice(request):
	return render(request, 'metStanice/metStanice.html',  {})
	#return render(request, '/a.html',  {})

def dajStanice(request):
	#Povuci sve metStanice iz baze
	stanice=WeatherStation.objects.all()
	# Konvertuj u geoJSON format
	stanice_dic= {
		"type":"FeatureCollection",
		"features":[stanice2geojson(stanica) for stanica in stanice],
	}
	return (JsonResponse(stanice_dic, safe=False))
	#return(HttpResponse("Ovde vrati geojson"))

#Metod koji objekat tipa WeatherStation pakuje u geoJSON
def stanice2geojson(stanica):
	return {
		"type":"Feature",
		"geometry": {	
			"type": "Point",
			#"coordinates": [5.883333333333333, 36.81666666666667],
			"coordinates":[stanica.geom.x, stanica.geom.y ],
		},
		"properties": {
			"name": stanica.name
		},
		"id": stanica.wmoid,
	}



