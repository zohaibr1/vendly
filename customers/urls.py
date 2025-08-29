from django.urls import path
from customers.views.customer_view import CustomerProfileView
urlpatterns = [
    path("me/",CustomerProfileView.as_view(),name="customer-profile")
]
