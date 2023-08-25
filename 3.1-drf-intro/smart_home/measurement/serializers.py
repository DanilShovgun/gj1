from rest_framework import serializers
from .models import Sensor, TemperatureMeasurement

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class TemperatureMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureMeasurement
        fields = '__all__'

