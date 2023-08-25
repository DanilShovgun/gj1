from rest_framework import viewsets
from .models import Sensor, TemperatureMeasurement
from .serializers import SensorSerializer, TemperatureMeasurementSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class TemperatureMeasurementViewSet(viewsets.ModelViewSet):
    queryset = TemperatureMeasurement.objects.all()
    serializer_class = TemperatureMeasurementSerializer