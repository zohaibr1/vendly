from django.contrib import admin
from .models import Payment, Refund
# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display=("id","order","payment_method","amount","status","vendor_amount","transaction_id","payment_date")
    list_filter=("payment_method","order","payment_date")
    readonly_fields=("admin_commission","vendor_amount","payment_date")
    search_fields=("transaction_id","order__id")

@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display=("id","payment","refund_amount","status","created_at","processed_at","processed_by")
    list_filter=("status","created_at")
    search_fields=("payment_id","reason","processed_by__username")
