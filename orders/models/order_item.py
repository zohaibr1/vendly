from django.db import models
from django.conf import settings
from decimal import Decimal
from products.models import Product
from orders.models import Order


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