from django.urls import path
from payments.views.payment_view import PaymentCreateView,PaymentDetailView
from payments.views.refund_views import RefundListView, RefundCreateView, RefundUpdateView

urlpatterns = [
    path("create/", PaymentCreateView.as_view(), name="payment_create"),
    path("<int:pk>/", PaymentDetailView.as_view(), name="payment_detail"),
    path("refunds/", RefundListView.as_view(), name="refund-list"),
    path("refunds/create/", RefundCreateView.as_view(), name="refund-create"),
    path("refunds/<int:pk>/update/", RefundUpdateView.as_view(), name="refund-update"),
]