from django.db import models
from django.conf import settings

class CustomerProfile(models.Model):
    """
    One-to-one profile for users with role == CUSTOMER.
    Keep it small for now; extend later (addresses, phone, preferences).
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="customer_profile"
    )
    phone = models.CharField(max_length=20, blank=True)
    default_address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Customer Profile"
        verbose_name_plural = "Customer Profiles"

    def __str__(self):
        return f"{self.user.username} profile"
