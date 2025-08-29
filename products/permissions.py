from rest_framework import permissions

class IsVendor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.vendor.user == request.user
    