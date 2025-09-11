from django.contrib import admin
from .models import Category, Zone, Device, Measurement, Alert, Organization

admin.site.register(Category)
admin.site.register(Zone)
admin.site.register(Device)
admin.site.register(Measurement)
admin.site.register(Alert)
admin.site.register(Organization)
