from rest_framework import generics,permissions,status
from rest_framework.response import Response
from products.models import ProductImage, Product
from products.serializers.product_serializer import ProductImageSerializer
from rest_framework.parsers import FormParser, MultiPartParser

class ProductImageUploadView(generics.CreateAPIView):
    serializer_class=ProductImageSerializer
    parser_classes=[FormParser,MultiPartParser]
    permission_classes=[permissions.IsAuthenticated]
    def perform_create(self, serializer):
            product_id=self.kwargs.get("pk")
            product=Product.objects.get(pk=product_id)

            if product.vendor.user != self.request.user:
                raise PermissionError("you are not Authorized!!")
            serializer.save(product=product)    

class ProductImageUpdateView(generics.UpdateAPIView):
     queryset=ProductImage.objects.all()
     serializer_class=ProductImageSerializer
     def perform_update(self, serializer):
          instance=self.get_object()
          
          if instance.product.vendor.user!=self.request.user:
               raise PermissionError("You cannot eidt image")
          serializer.save()

class ProductImageDeleteView(generics.DestroyAPIView):
     queryset=ProductImage.objects.all()
     serializer_class=ProductImageSerializer
     def perform_destroy(self, instance):
            
            if instance.product.vendor.user!=self.request.user:
               raise PermissionError("You cannot eidt image")
            instance.delete()
