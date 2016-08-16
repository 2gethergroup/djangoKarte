import csv #Modul za rad sa CSV podacima
from django.contrib.gis.geos import Point

from metStanice.models import WeatherStation
from django.contrib.gis.utils import LayerMapping


def dms2dec(value):
    """
    Degres Minutes Seconds to Decimal degres
    """
    degres, minutes, seconds = value.split()
    seconds, direction = seconds[:-1], seconds[-1]
    dec = float(degres) + float(minutes)/60 + float(seconds)/3600
    if direction in ('S', 'W'):
        return -dec
    return dec

def run():
	csv_file = '/home/nemanja/Fakultet/GisProgramiranje/djangoKarte/static_base/data/metStanice/stanice.csv'
	reader = csv.DictReader(open(csv_file, 'rt'), delimiter="\t")
	i=0
	for line in reader:
		lng = dms2dec(line.pop('Longitude'))
		lat = dms2dec(line.pop('Latitude'))
		wmoid = int(line.pop('StationId'))
		name = line.pop('StationName').title()

		WeatherStation (wmoid=wmoid, name=name, geom=Point(lng, lat)).save()
		i=i+1
		print(i)
	print ("Stanice su uspešno prepisane u bazu.")	