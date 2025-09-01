from rest_framework import generics,permissions,status
from rest_framework.response import Response
from storeface.models import Cart,CartItem
from storeface.views.cart_view import CartDetailView
from rest_framework.views import APIView
from orders.models import Order,OrderItem,ShippingAddress
from orders.serializers.order_serializer import OrderSerializer
from orders.serializers.order_item_serializer import OrderItemSerializer
from orders.serializers.shipping_address_serializer import ShippingAddressSerializer
from django.shortcuts import get_object_or_404

class CheckoutView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user=request.user 
        
        cart=Cart.objects.filter(customer=user).first()
        if not cart or cart.items.count()==0:
            return Response({"details":"Cart is empty. "},status=status.HTTP_400_BAD_REQUEST)
        
        shipping_id=request.data.get('shipping_address_id')
        if shipping_id:
            shipping_address=get_object_or_404(ShippingAddress, id=shipping_id, user=user)
        else:
            shipping_address=ShippingAddress.objects.filter(user=user, is_default=True).first()
            if not shipping_address:
                return Response({"error":"Shipping Address Required!"},status=status.HTTP_400_BAD_REQUEST)
            
        order=Order.objects.create(customer=user, address=shipping_address.address, city=shipping_address.city,postal_code=shipping_address.postal_code, country=shipping_address.country, phone=shipping_address.phone)
        
        for item in cart.items.all():
            OrderItem.objects.create(order=order, product=item.product,quantity=item.quantity,price=item.product.price)
        
        cart.items.all().delete()
        serializer=OrderSerializer(order)
        return Response(serializer.data,status=status.HTTP_201_CREATED)