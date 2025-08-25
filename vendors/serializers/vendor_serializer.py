from rest_framework import serializers
from models import VendorProfile

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = ['id', 'user', 'business_name', 'is_approved']
        read_only_fields = ['is_approved']  # vendors cannot approve themselves
