from rest_framework import generics,status,permissions
from storeface.serializers.cart_serializer import CartSerializer
from storeface.serializers.cart_item_serialzer import CartItemSerializer
from storeface.models.cart import Cart,CartItem
from storeface.utils import get_or_create_cart
from rest_framework.views import APIView
from rest_framework.response import Response

class CartDetailView(APIView):
    permission_classes=[permissions.AllowAny]
    def get(self, request):
        cart=get_or_create_cart(request)
        serialzer=CartSerializer(cart)
        return Response(serialzer.data)
    

class AddCartView(APIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        cart=get_or_create_cart(request)
        serializer=CartItemSerializer(data=request.data)
        if serializer.is_valid():
            product=serializer.validated_data["product"]
            quantity=serializer.validated_data.get("quantity",1)
            item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                item.quantity += quantity
                item.save()
            else:
                item.quantity = quantity
                item.save()

            return Response(CartSerializer(cart).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateCartItemView(generics.UpdateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes=[permissions.AllowAny]

class RemoveCartItemView(generics.DestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes=[permissions.AllowAny]

    def delete(self,request,item_id):
        try:
            item=CartItem.objects.get(id=item_id)
            item.delete()
            return Response({"message":"item deleted succefully"},status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response({"error":"item not found"},status=status.HTTP_404_NOT_FOUND)
class ClearCartView(APIView):
    permission_classes=[permissions.AllowAny]

    def delete(self, request):
        cart = get_or_create_cart(request)
        cart.items.all().delete()
        return Response({"detail": "Cart cleared."}, status=status.HTTP_204_NO_CONTENT)
    
