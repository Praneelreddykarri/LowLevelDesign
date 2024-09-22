from Folder import Folder
from File import File

class FileStorage:
    def __init__(self):
        self.storage = {}
        self.root = Folder("root")
        self.storage["/"] = self.root

    def add(self, path, item):
        parent_folder_path = '/'
        parent_folder = self.get_folder(parent_folder_path)
        if isinstance(item, Folder):
            parent_folder.add_folder(item)
        elif isinstance(item, File):  # Accept any item (including EncryptedFile)
            parent_folder.add_file(item)
        self.storage[path] = item

    def get_file(self, path):
        return self.storage.get(path)

    def get_folder(self, path):
        return self.storage.get(path)

    def delete(self, path):
        if path in self.storage:
            del self.storage[path]
            return True
        return False
