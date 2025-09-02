from rest_framework import serializers
from payments.models import Refund, Payment

class RefundSerializer(serializers.ModelSerializer):
    payment_id= serializers.IntegerField(write_only=True)
    class Meta:
        model=Payment
        fields=["id","payment_id","refunt_amount","reason","status","created_at","processed_at","processed_by",]
        ready_only_fields=["id","created_at","processed_at","status","processed_by"]

        def validate_payment_id(self,value):
            try:
                payment=Payment.objects.get(id-value)
            except payment.DoesNotExist:
                raise serializers.ValidationError("payment Not found")
            
            if payment.status != "SUCCESS":
                raise serializers.ValidationError("Refund only appleid for successfull payment!!")
            
            return value
    
    
    def validate(self, data):
        """Prevent refunding more than available"""
        payment = Payment.objects.get(id=data["payment_id"])
        total_refunded = sum(ref.refund_amount for ref in payment.refunds.all())
        if data["refund_amount"] + total_refunded > payment.amount:
            raise serializers.ValidationError("Refund amount exceeds original payment.")
        return data

    
    
    def create(self, validated_data):
        payment_id = validated_data.pop("payment_id")
        payment = Payment.objects.get(id=payment_id)
        refund = Refund.objects.create(payment=payment, **validated_data)
        return refund    