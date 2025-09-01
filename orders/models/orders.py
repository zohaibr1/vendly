from django.db import models
from django.conf import settings
from decimal import Decimal
from products.models import Product
class Order(models.Model):
    STATUS_CHOICES=(
        ("pending","pending"),
        ("processing","processing"),
        ("shipped","shipped"),
        ("delivered","delivered"),
        ("cancelled","cancelled")
    )
    customer=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    full_name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=10)
    country=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="pending")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["customer", "status"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"Order #{self.id} — {self.customer}"

    @property
    def total_price(self):
        # sum of items (quantity * captured price)
        return sum(item.total_price for item in self.items.all())
