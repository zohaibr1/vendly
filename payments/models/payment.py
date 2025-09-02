from django.db import   models
from decimal   import   Decimal
from vendors.models import VendorProfile
class Payment(models.Model):
    order=models.ForeignKey('orders.Order',related_name="payment", on_delete=models.CASCADE)
    # vendor = models.ForeignKey("vendors.VendorProfile", on_delete=models.CASCADE, related_name="payments")
    PAYMENT_METHOD= [("STRIPE","stripe"),("PAYPAL","paypal"),("COD","cash on delivery")]
    STATUS_CHOICE= [("PENDING","pending"),("SUCCESS","success"),("FAILED","failed")]
    payment_method= models.CharField(max_length=20, choices=PAYMENT_METHOD, default="STRIPE")
    amount=models.DecimalField(max_digits=20, decimal_places=2)
    status=models.CharField(max_length=20, choices=STATUS_CHOICE, default="PENDING")
    transaction_id=models.CharField(max_length=100, null=True, blank=True)
    payment_date=models.DateTimeField(auto_now_add=True)
    admin_commission = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False, default=0
    )
    vendor_amount = models.DecimalField(
        max_digits=10, decimal_places=2, editable=False, default=0
    )

    def save(self, *args, **kwargs):
        if self.amount:  
            self.admin_commission = (self.amount * Decimal("0.01")).quantize(Decimal("0.01"))
            self.vendor_amount = self.amount - self.admin_commission
        super().save(*args, **kwargs)
        if self.status == "SUCCESS":
            self.order.status = "processing"
            self.order.save(update_fields=["status"])
        elif self.status == "FAILED":
            self.order.status = "cancelled"
            self.order.save(update_fields=["status"])
   
    @property
    def refunded_amount(self):
        """Sum of all approved refunds"""
        return sum(refund.refund_amount for refund in self.refunds.filter(status="approved"))

    @property
    def final_vendor_amount(self):
        """Vendor payout after refunds"""
        return self.vendor_amount - self.refunded_amount

    def __str__(self):
        return f"Payment {self.id} - Net: {self.final_vendor_amount} - Order {self.order} - Status {self.status}"