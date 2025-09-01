from rest_framework import serializers
from orders.models import Order,OrderItem,ShippingAddress
from products.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "product", "product_name", "quantity", "price", "total_price"]
        read_only_fields = ["id", "price", "total_price", "product_name"]
