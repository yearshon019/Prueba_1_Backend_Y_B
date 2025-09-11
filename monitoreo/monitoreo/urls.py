from django.contrib import admin
from django.urls import path
from devices.views import dashboard, device_list, device_detail, measurement_list, alerts_week, login_view, logout_view, register_view, password_reset_request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('devices/device_list/', device_list, name='device_list'),
    path('devices/<int:device_id>/', device_detail, name='device_detail'),
    path('devices/measurements/', measurement_list, name='measurement_list'),
    path('alerts/week/', alerts_week, name="alerts_week"),

    # auth
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
    path('password-reset/', password_reset_request, name="password_reset"),
    ]
