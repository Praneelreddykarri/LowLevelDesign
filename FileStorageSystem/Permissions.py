class Permissions:
    def __init__(self):
        self.user_permissions = {}

    def set_permission(self, user, permission_type):
        self.user_permissions[user] = permission_type

    def check_permission(self, user, permission_type):
        return self.user_permissions.get(user) == permission_type
