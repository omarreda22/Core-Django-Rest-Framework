from rest_framework import permissions

from .permissions import IsStaffEditorPermissions


class IsStaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]
