from rest_framework import serializers
from .models import Product, ProductPosition, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description')


class ProductPositionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductPosition
        fields = ('id', 'product', 'storage_cost')


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ('id', 'name', 'positions')

    def create(self, validated_data):
        positions_data = validated_data.pop('positions')
        stock = Stock.objects.create(**validated_data)
        for position_data in positions_data:
            ProductPosition.objects.create(stock=stock, **position_data)
        return stock

    def update(self, instance, validated_data):
        positions_data = validated_data.pop('positions')
        positions = (instance.positions).all()
        positions = list(positions)
        
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        for position_data in positions_data:
            position = positions.pop(0)
            position.storage_cost = position_data.get('storage_cost', position.storage_cost)
            position.save()
        return instance

