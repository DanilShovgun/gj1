from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'warehouses', views.WarehouseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]