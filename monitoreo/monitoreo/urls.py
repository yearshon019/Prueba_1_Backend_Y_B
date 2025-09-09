from django.contrib import admin
from django.urls import path
from devices.views import dashboard, device_list, device_detail, measurement_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
    path('devices/device_list/', device_list, name='device_list'),
    path('devices/<int:device_id>/', device_detail, name='device_detail'),
    path('devices/measurements/', measurement_list, name='measurement_list'),
    ]
