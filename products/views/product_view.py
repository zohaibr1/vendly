from rest_framework import permissions, generics
from products.models.product import Product
from products.serializers.product_serializer import ProductSerializer
from products.permissions import IsVendor

class ProductListView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class= ProductSerializer
    permission_classes=[permissions.IsAuthenticated]
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]   

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user.vendor_profile)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[permissions.IsAuthenticated,IsVendor]