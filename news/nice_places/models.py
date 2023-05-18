from django.db import models
from django_admin_geomap import GeoItem

class Places(models.Model, GeoItem):
    name = models.CharField(max_length=255, verbose_name='Название места',
                            help_text='Введите название')
    lon = models.FloatField()  # долгота
    lat = models.FloatField()  # широта

    @property
    def geomap_longitude(self):
        return str(self.lon)

    @property
    def geomap_latitude(self):
        return str(self.lat)