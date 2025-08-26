from django.urls import path
from vendors.views.profile_view import VendorProfileView
from vendors.views.approval_view import VendorApprovalListView,VendorApprovalUpdateView
urlpatterns = [
    path("/profile/",VendorProfileView.as_view(),name="vendor-profile"),
    path("/approval/",VendorApprovalListView.as_view(),name="vendor-approval"),
    path("/approval/<int:pk>",VendorApprovalUpdateView.as_view(),name="vendor-approval-update"),
]
