from django.urls import path
from storeface.views.cart_view import CartDetailView,AddCartView,UpdateCartItemView,RemoveCartItemView,ClearCartView

urlpatterns = [
    path("",CartDetailView.as_view(),name="cart-detail"),
    path("cart/add/",AddCartView.as_view(),name="cart-add"),
    path("cart/<int:pk>/",UpdateCartItemView.as_view(),name="cart-update"),
    path("cart/remove/<item_id>/",RemoveCartItemView.as_view(),name="cart-remove"),
    path("cart/clear",ClearCartView.as_view(),name="cart-clear"),
]
