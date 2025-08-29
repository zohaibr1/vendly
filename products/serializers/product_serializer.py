from rest_framework import serializers
from products.models.product import Product
from products.models.product_image import ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields=["id","image","alt_text","uploaded_at"]
        read_only_fields=["id","product","uploaded_at"]

class ProductSerializer(serializers.ModelSerializer):
    images= ProductImageSerializer(many=True,read_only=True)
    class Meta:
        model=Product
        fields="__all__"
        read_only_fields=["vendor","slug","discount_price","created_at","updated_at"]
