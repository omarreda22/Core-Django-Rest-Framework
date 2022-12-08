from rest_framework import permissions

from .permissions import IsStaffEditorPermissions


class IsStaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]


class UserQuerySetMixin():
    user_field = 'user'

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data['user'] = user
        print(lookup_data)
        qs = super().get_queryset(*args, **kwargs)
        if user.is_superuser:
            return qs
        # if is_staff
        return qs.filter(**lookup_data)
