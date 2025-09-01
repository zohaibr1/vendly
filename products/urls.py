from django.urls import path
from products.views.product_view import ProductListView,ProductDetailView,ProductCreateView
from products.views.category_view import CategoryListView, CategoryDetailView 
from products.views.productImage_view import ProductImageUploadView,ProductImageUpdateView,ProductImageDeleteView
urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category-list-create"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("", ProductListView.as_view(), name="product-list"),
    path("create/", ProductCreateView.as_view(), name="products-create"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-details"),
    path("products/<int:pk>/upload-image/", ProductImageUploadView.as_view(), name="product-upload-image"),
    path("products/<int:pk>/update-image/", ProductImageUpdateView.as_view(), name="product-update-image"),
    path("products/<int:pk>/delete-image/", ProductImageDeleteView.as_view(), name="product-delete-image"),
]
