from django.db import models
from django.conf import settings
from products.models import Category
class VendorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="vendor_profile")
    store_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="vendors")
    contact_no = models.CharField(max_length=15)
    address = models.TextField()


    def __str__(self):
        return self.store_name
