

from django.contrib import admin
from django_admin_geomap import ModelAdmin
from .models import Places

class Admin(ModelAdmin):
    geomap_field_longitude = "id_lon"
    geomap_field_latitude = "id_lat"

admin.site.register(Places, Admin)