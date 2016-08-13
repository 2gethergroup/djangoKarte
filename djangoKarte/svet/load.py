
# Import modula LayerMapping
from django.contrib.gis.utils import LayerMapping
# Import definisanog modela
from .models import WorldBorder

# Rečnik korespodentnih polja
# Ključ naziv poja u bazi
# Vrednost polje u .shp fajlu
world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON',
}

#apsolutna putanja do podataka
world_shp = '/home/nemanja/Fakultet/GisProgramiranje/djangoKarte'\
            '/static_base/data/svet/data/TM_WORLD_BORDERS-0.3.shp'

#metod za prepisivaje podataka u bazu
def run(verbose=True):
    lm = LayerMapping(
        WorldBorder, world_shp, world_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)




    