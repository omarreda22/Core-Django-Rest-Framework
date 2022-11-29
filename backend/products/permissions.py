from rest_framework import permissions


class IsStaffEditorPermissions(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    """
    if you want delete this function "has_permission" you can type in view
    permission_classes = [IsAdminUser, IsStaffEditorPermissions]
    IsAdminUser -> this for make sure that user is from staff
    """

    def has_permission(self, request, view):
        # if not request.user.username == 'omarreda':
        #     return False
        print(request.user.username)
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)

    # def has_permission(self, request, view):
    #     user = request.user
    #     # print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm("products.view_product"): # app_name.action_modelName
    #             return True
    #         if user.has_perm("products.change.product"):
    #             return True
    #         if user.has_perm("products.add.product"):
    #             return True
    #         if user.has_perm("products.delete.product"):
    #             return True
    #         return False
    #     return False
