from rest_framework import status,generics
from rest_framework.response import response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from vendors.models import VendorProfile
from vendors.serializers.vendor_serializer import VendorSerializer

class VendorApprovalListView(generics.ListAPIView):
    queryset = VendorProfile.objects.filter(user__vendor_approved=False)
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class VendorApprovalUpdateView(generics.ListAPIView):
    queryset=VendorProfile.objects.filter(user_vendor_approved=False)
    serializer_class=VendorSerializer
    permission_classes=[IsAuthenticated,IsAdminUser]

    def update(self, request,*args, **kwargs):
        vendor_profile=self.get_object()
        action=request.data.get("action")
        if action=="approve":
            vendor_profile.user.vendor_approved=True
            vendor_profile.user.save()
            return response({'status':'vendor approved'})
        elif action=="reject":
            vendor_profile.user.vendor_approved= False
            vendor_profile.user.save()
            return response({'status':'Rejected'})
        else:
            return response({'error':'inValid Actions'},status=status.HTTP_400_BAD_REQUEST)