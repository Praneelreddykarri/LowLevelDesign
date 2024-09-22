from Permissions import Permissions

class File:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.versions = [data]
        self.shared_with = []
        self.permissions = Permissions()

    def update(self, new_data):
        self.data = new_data
        self.versions.append(new_data)  # Save the new version


    def share(self, user):
        self.shared_with.append(user)

    def get_data(self):
        return self.data

    def set_permission(self, user, permission_type):
        self.permissions.set_permission(user, permission_type)

    def check_permission(self, user, permission_type):
        return self.permissions.check_permission(user, permission_type)

    def get_version(self, version_index):
        if version_index < len(self.versions):
            return self.versions[version_index]

