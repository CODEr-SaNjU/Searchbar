from django.shortcuts import render, redirect
from django.contrib.gis.db.models.functions import Distance
from .models import *
from django.contrib.gis.geos import Point
from .forms import RestaurantRegForm
import googlemaps
gmps = googlemaps.Client(key='AIzaSyC43U2-wqXxYEk1RBrTLdkYt3aDoOxO4Fw')


def home(request):
    if request.method == "POST":
        r = request.POST['locationsearch']
        geocode_result = gmps.geocode(r)
        for i in geocode_result:
            add = i['formatted_address']
            print(add)
            x = i['geometry']
            y = x['location']
            lat = y['lat']
            lon = y['lng']
            print(lat, lon)
        user_location = Point(lon, lat, srid=4326)
        user_city = add
        queryset = RestaurantReg.objects.annotate(distance=Distance('restaurant_location',
                                                                    user_location)/1000
                                                ).order_by('distance')[0:6]
        return render(request, 'frontend/base.htm',  {'queryset': queryset, 'user_city': user_city})

    else:
        return render(request, 'frontend/base.htm')


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


api_key = 'AIzaSyDo19usvpLpA6NqavX9_srpMsPqQonJdec'
