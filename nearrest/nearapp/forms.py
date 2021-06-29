from django import forms
from django.db.models.query import QuerySet
from django.forms import fields, widgets
from .models import *
from django.contrib.gis import forms


class RestaurantRegForm(forms.ModelForm):
    class Meta:
        model = RestaurantReg
        fields = '__all__'
        restaurant_location = forms.PolygonField()
        labels = {
            'restaurant_name': ('Restaurant Name'),
            'restaurant_location': ('Restaurant Location'),
            'restaurant_number': ('Restaurant Number'),
            'restaurant_address': ('Restaurant Address'),
            'restaurant_city': ('Restaurant City'),
            'restaurant_web': ('Restaurant website')
        }
        widgets = {
            'restaurant_name': forms.TextInput(attrs={'type': 'text', 'autocomplete': "off", 'class': 'form-control'}),
            'restaurant_location': forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500, 'class': 'form-control', }),
            'restaurant_number': forms.TextInput(attrs={'type': 'number', 'autocomplete': "off",  'class': 'form-control', 'placeholder': 'Please Enter  Number here', 'required': True}),
            'restaurant_address': forms.Textarea(attrs={'type': 'text', 'autocomplete': "off", 'class': 'form-control', 'rows': '3', 'cols': '3'}),
            'restaurant_city': forms.TextInput(attrs={'type': 'text', 'autocomplete': "off", 'class': 'form-control'}),
            'restaurant_web': forms.TextInput(attrs={'type': 'url', 'autocomplete': "off", 'class': 'form-control'}),
        }
