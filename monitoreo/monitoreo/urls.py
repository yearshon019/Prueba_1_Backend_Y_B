from django.contrib import admin
from django.urls import path
from dispositivos.views import dashboard, device_list, device_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
    path('dispositivos/device_list/', device_list, name='device_list'),
    path('dispositivos/<int:device_id>/', device_detail, name='device_detail'),
    ]
