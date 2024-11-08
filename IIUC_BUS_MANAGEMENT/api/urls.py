
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('driver_view',views.driver_view,name="driver_view"),
    path('driver_insert',views.driver_insert,name="driver_insert"),
    path('dashboard',views.Dashboard,name="dashboard"),
]
