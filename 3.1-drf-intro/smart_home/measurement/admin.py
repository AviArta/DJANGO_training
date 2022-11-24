from django.contrib import admin

# Register your models here.
from measurement.models import Sensor, Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'discription']

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['sensor_id', 'temperature', 'created_at']