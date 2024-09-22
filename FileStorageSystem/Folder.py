class Folder:
    def __init__(self, name):
        self.name = name
        self.contents = {}

    def add_file(self, file):
        self.contents[file.name] = file

    def add_folder(self, folder):
        self.contents[folder.name] = folder
