from django.db import models

class ProductImage(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/")
    alt_text = models.CharField(max_length=255, blank=True)
    is_feature = models.BooleanField(default=False)  # first/main image flag
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-is_feature", "uploaded_at")
