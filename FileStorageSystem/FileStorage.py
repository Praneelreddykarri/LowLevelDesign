from Folder import Folder
from File import File
import threading

class FileStorage:

    _instance=None
    _lock=threading.Lock()

    def __new__(cls):
        if(cls._instance is None):
            cls._lock.acquire()
            if (cls._instance is None):
                cls._instance = super().__new__(cls)
                cls._instance.storage = {}
            cls._lock.release()
        return cls._instance

    def __init__(self):
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
