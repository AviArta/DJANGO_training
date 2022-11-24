from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=30)
    discription = models.CharField(max_length=300)


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField()
    nullable = models.ImageField(upload_to='C:/Users/kuvsh/Desktop/HELP_Files', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)