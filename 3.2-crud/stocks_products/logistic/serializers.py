from rest_framework import serializers
from .models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description')

class StockProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = StockProduct
        fields = ('id', 'product', 'price', 'quantity')

class StockSerializer(serializers.ModelSerializer):
    positions = StockProductSerializer(many=True, read_only=True)

    class Meta:
        model = Stock
        fields = ('id', 'address', 'positions')

    def create(self, validated_data):
        positions_data = validated_data.pop('positions', [])
        stock = Stock.objects.create(**validated_data)
        for position_data in positions_data:
            StockProduct.objects.create(stock=stock, **position_data)
        return stock

    def update(self, instance, validated_data):
        positions_data = validated_data.pop('positions', [])
        instance.address = validated_data.get('address', instance.address)
        instance.save()

        for position_data in positions_data:
            position = StockProduct.objects.get(id=position_data['id'])
            position.price = position_data.get('price', position.price)
            position.quantity = position_data.get('quantity', position.quantity)
            position.save()

        return instance
