from django.conf    import settings
from django.db      import models


class WishList(models.Model):
    customer=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='whishlist_item',on_delete=models.CASCADE)
    product=models.ForeignKey('products.Product',on_delete=models.CASCADE, related_name="wishlist_by")
    added_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("customer", "product")
        verbose_name = "Wishlist Item"
        verbose_name_plural = "Wishlist Items"


    def __str__(self):
        return f"{self.customer.username} → {self.product.name}"