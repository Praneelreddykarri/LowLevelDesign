from abc import ABC, abstractmethod
from EncryptedFile import EncryptedFile
from File import File
from Folder import Folder

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class UpdateCommand(Command):
    def __init__(self, file, new_data):
        self.file = file
        self.new_data = new_data

    def execute(self):
        self.file.update(self.new_data)
        print(f"Updated new data to {self.file.name}.")

class DeleteCommand(Command):
    def __init__(self, storage, path):
        self.storage = storage
        self.path = path

    def execute(self):
        if self.storage.delete(self.path):
            print(f"Deleted {self.path}.")
        else:
            print(f"No file found at {self.path}.")

class ShareCommand(Command):
    def __init__(self, file, users_to_share, permission_type="read"):
        self.file = file
        self.users_to_share = users_to_share
        self.permission_type = permission_type

    def execute(self):
        for user in self.users_to_share:
            self.file.share(user)
            self.file.set_permission(user, self.permission_type)
            print(f"Sharing {self.file.name} with {user} and granted {self.permission_type} permission.")

class CreateFolderCommand(Command):
    def __init__(self, storage, parent_path, folder_name):
        self.storage = storage
        self.parent_path = parent_path
        self.folder_name = folder_name

    def execute(self):
        new_folder = Folder(self.folder_name)
        self.storage.add(f"{self.parent_path}/{self.folder_name}", new_folder)
        print(f"Created folder {self.folder_name} in {self.parent_path}.")

class CreateFileCommand(Command):
    def __init__(self, storage, path, file_name, file_data):
        self.storage = storage
        self.path = path
        self.file_name = file_name
        self.file_data = file_data

    def execute(self):
        new_file = File(self.file_name, self.file_data)
        self.storage.add(f"{self.path}/{self.file_name}", new_file)
        print(f"Created file {self.file_name} in {self.path}.")