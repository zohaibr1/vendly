from django.urls import path
from orders.views.checkout_view import CheckoutView
from orders.views.shipping_address_view import ShippingListCreateView,ShippingDetailView
from orders.views.order_view import OrderListView,OrderDetailView,OrderStatusUpdateView
urlpatterns = [
    path('checkout/',CheckoutView.as_view(),name="checkout"),
    path('shipping_address/',ShippingListCreateView.as_view(),name="shipping_address_list"),
    path('shipping_address/<int:pk>/',ShippingDetailView.as_view(),name="shipping_address"),
    path('order/',OrderListView.as_view(),name="order_list"),
    path('order/<int:pk>/',OrderDetailView.as_view(),name="order-detail"),
    path('order/<int:pk>/status/',OrderStatusUpdateView.as_view(),name="order-update"),

]
