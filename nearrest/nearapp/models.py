from django.db import models
from django.contrib.gis.db import models
# Create your models here.


class RestaurantReg(models.Model):
    restaurant_name = models.CharField(max_length=300)
    restaurant_location = models.PointField()
    restaurant_number = models.CharField(unique=True, max_length=14)
    restaurant_address = models.CharField(max_length=100)
    restaurant_city = models.CharField(max_length=50)
    restaurant_web = models.URLField(unique=True)

    def __str__(self):
        return self.restaurant_name
