from rest_framework import serializers

from shop.models import Product, Category
from orders.models import Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    order = serializers.CharField(source='order.address')
    product = serializers.CharField(source='product.name')

    class Meta:
        model = OrderItem
        fields = '__all__'
