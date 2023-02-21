# this file is a custom permissions

from rest_framework import permissions

class IsAdminOrReadOnlyPermissions(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        #condition permission
        # admin_permissions = bool(request.user and request.user.is_staff)
        # return request.method == "GET" or admin_permissions
        
        # safe method means READ_ONLY, unsafe can do CRUD operations
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
           return bool(request.user and request.user.is_staff)
    
class IsReviewUserOrReadOnlyPermission(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # safe method means READ_ONLY, unsafe can do CRUD operations
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
           return obj.review_user == request.user