
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('driver_insert',views.driver_insert,name="driver_insert"),
    path('bus_update',views.bus_update,name="bus_update"),
    path('driver_view',views.driver_view,name="driver_view"),
    path('search_trip',views.search_trip,name="search_trip"),
]
