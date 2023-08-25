from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)

class TemperatureMeasurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)