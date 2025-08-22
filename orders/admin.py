from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ("user", "full_name", "city", "country", "is_default", "updated_at")
    list_filter = ("is_default", "country")
    search_fields = ("full_name", "address", "city", "postal_code", "phone", "user__username", "user__email")


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("total_price",)
    fields = ("product", "quantity", "price", "total_price")
    readonly_fields=("total_price",)
    class Media:
        js=("Order/js/OrderItem.js",) #used for autofill for Js

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "status", "created_at", "order_total")
    list_filter = ("status", "created_at")
    search_fields = ("id", "customer__username", "customer__email", "full_name", "address", "city")
    inlines = [OrderItemInline]
    readonly_fields = ("created_at", "updated_at")

    def order_total(self, obj):
        return obj.total_price
    order_total.short_description = "Total"
