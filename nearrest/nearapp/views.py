from django.shortcuts import render, redirect
from django.contrib.gis.db.models.functions import Distance
from .models import *
from django.contrib.gis.geos import Point
from .forms import RestaurantRegForm
longitude = 76.61727904206835
latitude = 27.23662089731647
user_location = Point(longitude, latitude, srid=4326)


def home(request):
    queryset = RestaurantReg.objects.annotate(distance=Distance('restaurant_location',
                                                                user_location)
                                              ).order_by('distance')[0:6]
    return render(request, 'frontend/base.htm',  {'queryset': queryset})


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
