
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('driver_view',views.driver_view,name="driver_view"),
    path('driver_insert',views.driver_insert,name="driver_insert"),
    path('dashboard',views.Dashboard,name="dashboard"),
    # Bus
    path('bus_view',views.bus_view,name="bus_view"),
    path('total_distance',views.total_distance,name="total_distance"),
    path('efficiency',views.efficiency,name="efficiency"),
    # Trip
    path('trip_view',views.trip_view,name="trip_view"),
    path('trip_insert',views.trip_insert,name="trip_insert"),
    path('looklike',views.look_like,name="look_like"),
    

]
