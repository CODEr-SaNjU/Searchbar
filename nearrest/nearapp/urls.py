from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('addrestaurant/', views.addrestaurant, name='addrestaurant')
]
