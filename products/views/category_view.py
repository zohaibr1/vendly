from rest_framework import generics, permissions
from products.serializers.catagory_serializer import CategorySerializer
from products.models.category import Category
class CategoryListView(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    def get_permissions(self):
        if self.request.method==['POST','PUT','DELETE','PATCH']:
            return [permissions.IsAdminUser()]
        return[permissions.AllowAny()]
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset=Category.objects.all()
        serializer_class=CategorySerializer
        def get_permissions(self):
            if self.request.method==['PUT','DELETE','PATCH']:
                return [permissions.IsAdminUser()]
            return[permissions.AllowAny()]
        