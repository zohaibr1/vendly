from django.contrib import admin
from .models import Category, Product, ProductImage

class ProductImageInline(admin.TabularInline):  # or admin.StackedInline if you want larger fields
    model = ProductImage
    extra = 1  # how many empty image fields show by default
    fields = ("image", "is_feature")  # show only relevant fields

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","name", "vendor", "price", "discount_price", "stock", "offer", "is_active", "created_at")
    list_filter = ("is_active", "category", "vendor", "offer")
    search_fields = ("name", "vendor__user__username", "vendor__user__email")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageInline]

    readonly_fields = ("discount_price",)  # ✅ vendors can’t edit it manually
    def final_price(self, obj):
        return obj.final_price
    final_price.short_description = "Final Price"

    
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "is_feature", "uploaded_at")
