from django.core.validators import MinValueValidator
from django.db import models

from rest_framework import viewsets
from .models import Product, Warehouse
from .serializers import ProductSerializer, WarehouseSerializer

class ProductViewSet(viewsets.ModelViewSet):  
    queryset = Product.objects.all()  
    serializer_class = ProductSerializer

class WarehouseViewSet(viewsets.ModelViewSet):  
    queryset = Warehouse.objects.all()  
    serializer_class = WarehouseSerializer

class Product(models.Model):
    title = models.CharField(max_length=60, unique=True)
    description = models.TextField(null=True, blank=True)


class Stock(models.Model):
    address = models.CharField(max_length=200, unique=True)
    products = models.ManyToManyField(
        Product,
        through='StockProduct',
        related_name='stocks',
    )


class StockProduct(models.Model):
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name='positions',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='positions',
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
