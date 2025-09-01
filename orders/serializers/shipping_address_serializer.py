from rest_framework import serializers
from orders.models import Order,OrderItem,ShippingAddress
from products.models import Product


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ["id","full_name","address","city","postal_code","country","phone", "is_default",]
        read_only_fields = ["id"]


