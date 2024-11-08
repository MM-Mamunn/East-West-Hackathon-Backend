
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('driver_view',views.driver_view,name="driver_view"),
    path('dashboard',views.Dashboard,name="dashboard"),
]
