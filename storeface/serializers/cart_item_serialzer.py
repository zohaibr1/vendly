from rest_framework import serializers
from storeface.models import CartItem,Cart
from products.serializers.product_serializer import ProductSerializer
from products.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    product=ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),  source="product", write_only=True)
    class Meta:
        model=CartItem
        fields=["id","product","product_id","quantity","subtotal"]

        read_only_fields=["id","subtotal","product"]
    