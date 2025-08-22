from django.db import models
from django.conf import settings

class ShippingAddress(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, related_name="shipping_address", on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=10)
    country=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    is_default=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-is_default", "-updated_at"]
        indexes = [
            models.Index(fields=["user", "is_default"]),
        ]
    def __str__(self):
        label= "(default)" if self.is_default else ""
        return f"{self.full_name},{self.address},{self.city}{label}"
    