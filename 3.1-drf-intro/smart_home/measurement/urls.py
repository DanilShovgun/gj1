from django.urls import include, path
from rest_framework import routers
from .views import SensorViewSet, TemperatureMeasurementViewSet

router = routers.DefaultRouter()
router.register(r'sensors', SensorViewSet)
router.register(r'temperature-measurements', TemperatureMeasurementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
