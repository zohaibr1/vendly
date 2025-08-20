from django.contrib import admin
from .models.customer  import CustomerProfile
from .models.wishList import WishList
@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "city", "country", "created_at")
    search_fields = ("user__username", "user__email", "phone")
@admin.register(WishList)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("customer", "product", "added_at")
    list_filter = ("added_at",)
    search_fields = ("customer__username", "product__name")