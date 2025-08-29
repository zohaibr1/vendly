# products/models/product.py

from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    vendor = models.ForeignKey("vendors.VendorProfile", on_delete=models.CASCADE, related_name="products")
    category = models.ForeignKey("products.Category", on_delete=models.SET_NULL, null=True, blank=True, related_name="products")
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    offer = models.PositiveIntegerField(default=0, help_text="Discount percentage (0–100)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def final_price(self):
        """Returns the price after applying discount (if any)."""
        if self.discount_price:
            return self.discount_price
        return self.price
    def save(self, *args, **kwargs):
        # Auto-generate slug
        if not self.slug:
            self.slug = slugify(self.name)

        # Auto-calculate discount_price if offer is set
        if self.offer > 0:
            discount_amount = (self.price * self.offer) / 100
            self.discount_price = self.price - discount_amount
        else:
            self.discount_price = None

        super().save(*args, **kwargs)   

    def __str__(self):
        return self.name


class Offer(models.Model):
    vendor = models.ForeignKey('vendors.VendorProfile', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="offers")
    discount_type = models.CharField(max_length=20, choices=[('percentage', 'Percentage'), ('flat', 'Flat')])
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def is_active(self):
        from django.utils import timezone
        return self.start_date <= timezone.now() <= self.end_date