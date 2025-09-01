from django.urls import path
from orders.views.checkout_view import CheckoutView
from orders.views.shipping_address_view import ShippingListCreateView,ShippingDetailView

urlpatterns = [
    path('checkout/',CheckoutView.as_view(),name="checkout"),
    path('shipping_address/',ShippingListCreateView.as_view(),name="shipping_address_list"),
    path('shipping_address/<int:pk>/',ShippingDetailView.as_view(),name="shipping_address"),
]
