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


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("products.Product", on_delete=models.PROTECT, related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self,*args, **kwargs):
        if self.price and self.product:
            self.price=self.product.price
        super().save(*args, **kwargs)
    class Meta:
        indexes = [
            models.Index(fields=["order"]),
            models.Index(fields=["product"]),
        ]

    def __str__(self):
        return f"{self.quantity} × {self.product}"

    @property
    def total_price(self):
        if self.price is None:
            return Decimal("0.00")
        return self.quantity * self.price