from rest_framework import generics,status,permissions
from rest_framework.response import Response
from orders.serializers.shipping_address_serializer import ShippingAddressSerializer
from orders.models import ShippingAddress

class ShippingListCreateView(generics.ListCreateAPIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ShippingAddressSerializer
    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ShippingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ShippingAddressSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user) 