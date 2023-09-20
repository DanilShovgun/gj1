from rest_framework import viewsets 
from .serializers import ProductSerializer, WarehouseSerializer
from .models import Product, Warehouse
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

class WarehouseViewSet(viewsets.ModelViewSet):
    serializer_class = WarehouseSerializer
    queryset = Warehouse.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['products__id']
