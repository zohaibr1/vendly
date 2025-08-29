from rest_framework import generics,status,permissions
from customers.models import CustomerProfile, WishList
from customers.serializers.customer_serializers import CustomerSerializer

class CustomerProfileView(generics.RetrieveUpdateAPIView):
    serializer_class=CustomerSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user.customer_profile