from File import File

class FileDecorator(File):
    def __init__(self, file: File):
        self._file = file

    def upload(self, new_data: str):
        self._file.upload(new_data)

    def get_data(self):
        return self._file.data

    def get_name(self):
        return self._file.name
