from rest_framework import generics,status,permissions
from rest_framework.response import responses
from payments.models import Payment
from payments.serializers.payment_serializer import PaymentSerializer

class PaymentCreateView(generics.CreateAPIView):
    serializer_class=PaymentSerializer
    permission_classes=[permissions.IsAuthenticated]
    
class PaymentDetailView(generics.UpdateAPIView):
    serializer_class=PaymentSerializer
    permission_classes=[permissions.IsAuthenticated]
    queryset=Payment.objects.all()
    
    def perform_update(self, serializer):
        payment=serializer.save()
        order=payment.order
        
        if payment.status == "SUCCESS":
            order.status = "processing"
        
        elif payment.status == "FAILED":
            order.status = "cancelled"
        
        order.save()