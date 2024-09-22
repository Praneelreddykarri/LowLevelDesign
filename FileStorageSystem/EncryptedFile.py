

class EncryptedFile:
    def __init__(self, file):
        self.file = file

    def update(self, new_data):
        encrypted_data = self.encrypt(new_data)
        self.file.update(encrypted_data)

    def get_data(self):
        encrypted_data = self.file.get_data()
        return self.decrypt(encrypted_data)

    def encrypt(self, data):
        # Simple character shifting for encryption
        return ''.join(chr(ord(char) + 1) for char in data)

    def decrypt(self, data):
        # Reversing the encryption
        return ''.join(chr(ord(char) - 1) for char in data)

    def set_permission(self, user, permission_type):
        self.file.set_permission(user, permission_type)

    def check_permission(self, user, permission_type):
        return self.file.check_permission(user, permission_type)

    @property
    def name(self):
        return self.file.name

    @property
    def version_history(self):
        return self.file.version_history

    @property
    def shared_with(self):
        return self.file.shared_with

    def share(self, user):
        self.file.share(user)

    def get_version(self, version_index):
        # Get the decrypted version of a specific index
        encrypted_version = self.file.get_version(version_index)
        if encrypted_version is not None:
            return self.decrypt(encrypted_version)
        return None
