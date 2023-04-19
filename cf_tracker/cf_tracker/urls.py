from api import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', views.car_travel),
    path('flight/', views.plane_travel),
    path('motorbike/', views.motorbike_travel),
    path('publictransit/', views.public_transit_travel),
    path('food/', views.food),s
]