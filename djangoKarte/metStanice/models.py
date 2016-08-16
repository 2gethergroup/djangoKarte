from django.contrib.gis.db import models 

class WeatherStation(models.Model):

    wmoid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    geom = models.PointField()

    def __str__(self):
        return self.name

