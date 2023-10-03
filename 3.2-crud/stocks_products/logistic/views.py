from rest_framework import viewsets 
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProductSerializer, StockSerializer
from .models import Product, Stock

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

class StockViewSet(viewsets.ModelViewSet):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['products__id']
