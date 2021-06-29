from django.shortcuts import render, redirect
from django.contrib.gis.db.models.functions import Distance
from .models import *
from django.contrib.gis.geos import Point
from .forms import RestaurantRegForm
from ip2geotools.databases.noncommercial import DbIpCity
import socket
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)


r = DbIpCity.get('157.38.4.207', api_key='free')


longitude = r.longitude
latitude = r.latitude
print(longitude, latitude)
user_location = Point(longitude, latitude, srid=4326)


def home(request):
    user_city = r.city
    queryset = RestaurantReg.objects.annotate(distance=Distance('restaurant_location',
                                                                user_location)/1000
                                              ).order_by('distance')[0:6]

    for query in queryset:
        dist = query.distance
        if dist <= 861:
            print(query)
    return render(request, 'frontend/base.htm',  {'queryset': queryset, 'user_city': user_city})


def addrestaurant(request):
    if request.method == "POST":
        form = RestaurantRegForm(request.POST)
        restaurant_number = request.POST['restaurant_number']
        if RestaurantReg.objects.filter(restaurant_number=restaurant_number).exists():
            RestaurantRegForm.error(
                request, "restaurant number address already exists ")
            return redirect('/')
        else:
            if form.is_valid():
                formsave = form.save()
                return redirect('/')

    else:
        form = RestaurantRegForm()
    return render(request, 'frontend/addrestaurant.htm', {'form': form})
