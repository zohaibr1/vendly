from rest_framework import serializers
from payments.models import Payment
from orders.models import Order

class PaymentSerializer(serializers.ModelSerializer):
    order_id=serializers.IntegerField(write_only=True)
    class Meta:
        model=Payment
        fields="__all__"
        read_only_fields = ["id", "payment_date", "admin_commission", "vendor_amount","order"]
    
    def validate_order_id(self, value):
        try:
            order = Order.objects.get(id=value)
        except Order.DoesNotExist:
            raise serializers.ValidationError("Order not found")
        return value

    def create(self, validated_data):
        order_id = validated_data.pop("order_id")
        order = Order.objects.get(id=order_id)

        # set order total as amount if not passed
        if not validated_data.get("amount"):
            validated_data["amount"] = order.total_price

        payment = Payment.objects.create(order=order, **validated_data)

        # auto update order status on successful payment
        if payment.status == "SUCCESS":
            order.status = "processing"
            order.save()

        return payment