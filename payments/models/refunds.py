from django.db import models
from django.conf import settings
from .payment import Payment
from django.utils import timezone
class Refund(models.Model):
    payment=models.ForeignKey(Payment,related_name="refunds", on_delete=models.CASCADE)
    refund_amount=models.DecimalField(max_digits=20, decimal_places=2)
    reason=models.TextField(null=True, blank=True)
    STATUS_CHOICE=[("PENDING","pending"),("APPROVED","approved"),("REJECTED","rejected")]
    status=models.CharField(max_length=50, choices=STATUS_CHOICE, default="pending")
    created_at=models.DateTimeField(auto_now_add=True)
    processed_at=models.DateTimeField(null=True, blank=True)
    processed_by=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,blank=True,null=True, related_name="processed_funds")

    def save(self, *args, **kwargs):
        if self.status == "approved" and not self.processed_at:
            self.processed_at = timezone.now()

        # Adjust payment balances
            self.payment.vendor_amount -= self.refund_amount
            self.payment.admin_commission -= (self.refund_amount * 0.01)  # rollback commission
            self.payment.save()

        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.id} - {self.status} - {self.refund_amount}"
    