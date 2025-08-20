from django.contrib import admin
from .models import VendorProfile
from django.contrib.auth import get_user_model
# Register your models here.

User=get_user_model()

class VendorProfileInline(admin.StackedInline):
    model = VendorProfile
    can_delete = False
    verbose_name_plural = "Vendor Profile"

# Extend UserAdmin to include VendorProfile
class UserAdminWithVendor(admin.ModelAdmin):
    inlines = [VendorProfileInline]
    list_display = ("username", "email", "role", "is_active", "is_staff")

# Unregister default User and register custom one with Vendor inline
admin.site.unregister(User)
admin.site.register(User, UserAdminWithVendor)
