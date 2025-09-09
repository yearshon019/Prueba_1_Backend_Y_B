
from django.shortcuts import render, get_object_or_404
from .models import Device, Category, Measurement, Alert, Zone
from django.db.models import Count
from django.core.paginator import Paginator

def dashboard(request):
    latest_measurements = Measurement.objects.select_related('device').order_by('-date')[:10]
    device_by_category = Category.objects.annotate(count=Count('device'))
    device_by_zone = Zone.objects.annotate(count=Count('device'))
    alerts_by_level = Alert.objects.values('alert_level').annotate(count=Count('id'))

    return render(request, 'device/inicio.html', {
        'latest_measurements': latest_measurements,
        'device_by_category': device_by_category,
        'device_by_zone': device_by_zone,
        'alerts_by_level': alerts_by_level,
    })



def device_detail(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    measurements = Measurement.objects.filter(device=device).order_by('-date')
    alerts = Alert.objects.filter(device=device).order_by('-date')

    return render(request, 'device/device_detail.html', {
        'device': device,
        'measurements': measurements,
        'alerts': alerts,
    })






def device_list(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()

    if category_id:
        devices = Device.objects.filter(category_id=category_id)
    else:
        devices = Device.objects.all()

    return render(request, 'device/device_list.html', {
        'devices': devices,
        'categories': categories,
        'selected_category': category_id
    })


def measurement_list(request):
    measurements = Measurement.objects.select_related('device').order_by('-date')
    paginator = Paginator(measurements, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'device/measurement_list.html', {'page_obj': page_obj})