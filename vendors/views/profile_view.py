from rest_framework import permissions,generics
from rest_framework.response import response
from serializers.vendor_serializer import VendorSerializer
from vendors.models import VendorProfile
from vendors.permissions import IsVendor


class VendorProfileView(generics.RetrieveUpdateAPIView):
    queryset=VendorProfile.objects.all()
    serializer_class=VendorSerializer
    permission_classes=[permissions.IsAuthenticated, IsVendor]


    def get_object(self):
        return self.request.user.vendor_profile
    