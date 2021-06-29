from django.contrib import admin
from .models import *
from django.contrib.gis.admin import OSMGeoAdmin
# Register your models here.


@admin.register(RestaurantReg)
class RestaurantRegAdmin(OSMGeoAdmin):
    list_display = ('restaurant_name', 'restaurant_location',
                    'restaurant_number')
