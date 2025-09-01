from rest_framework import serializers
from storeface.models import CartItem,Cart
from products.serializers.product_serializer import ProductSerializer
from products.models import Product
from.cart_item_serialzer import CartItemSerializer

class CartSerializer(serializers.ModelSerializer):
    items=CartItemSerializer(many=True, read_only=True)

    class Meta:
        model=Cart
        fields="__all__"
        read_only_fields=["id","customer","session_key","items","total_items","total_price",]

