from rest_framework import generics,status,permissions
from rest_framework.response import Response
from orders.models import Order,OrderItem,shipping_address
from orders.serializers.order_serializer import OrderSerializer
from orders.serializers.order_item_serializer import OrderItemSerializer
from orders.serializers.shipping_address_serializer import ShippingAddressSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

class OrderListView(generics.ListAPIView):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=OrderSerializer
    
    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by("-created_at")
    

class OrderDetailView(generics.RetrieveAPIView):
        permission_classes=[permissions.IsAuthenticated]
        serializer_class=OrderSerializer
        def get_queryset(self):
            return Order.objects.filter(customer=self.request.user)


class OrderStatusUpdateView(APIView):
    permission_classes=[permissions.IsAdminUser]
    def patch(self, request,pk):
        order=get_object_or_404(Order, pk=pk)
        new_status=request.data.get("status")
        if new_status not in dict(Order.STATUS_CHOICES):
            return Response({"Error":"Invalid Status Choice"},status=status.HTTP_400_BAD_REQUEST)
        
        order.status=new_status
        order.save()
        return Response({"message":f"Order {order.id} updated to {order.status}"})