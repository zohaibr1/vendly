from rest_framework import serializers
from customers.models import CustomerProfile

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomerProfile
        fields="__all__"
        read_only_fields=["id","user","created_at","updated_at"]
