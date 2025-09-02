from rest_framework import generics, permissions
from payments.models import Refund
from payments.serializers import RefundSerializer


class RefundCreateView(generics.CreateAPIView):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer
    permission_classes = [permissions.IsAuthenticated]



class RefundListView(generics.ListAPIView):
    serializer_class = RefundSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:  
            return Refund.objects.all()
        return Refund.objects.filter(payment__order__user=user)


# Admin can approve/reject
class RefundUpdateView(generics.UpdateAPIView):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        refund = serializer.save(processed_by=self.request.user)
        return refund
