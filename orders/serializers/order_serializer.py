from rest_framework import serializers
from orders.models import Order,OrderItem,ShippingAddress
from products.models import Product
from orders.serializers.order_item_serializer import OrderItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = Order
        fields = [
            "id","customer","full_name","address","city","postal_code","country","phone", "status","created_at","updated_at","items","total_price",]
        read_only_fields = ["id", "status", "created_at", "updated_at", "items", "total_price"]
