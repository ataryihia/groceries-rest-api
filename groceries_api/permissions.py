from rest_framework import permissions

class updateOwnProfile(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
        """check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class updateOwnGroceries(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
        """check user is trying to edit their own grocerie"""

        return obj.id == request.user.id
