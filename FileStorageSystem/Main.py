from FileStorage import FileStorage
from EncryptedFile import EncryptedFile
from Command import ShareCommand
from Command import UpdateCommand
from Command import DeleteCommand
from Command import CreateFolderCommand
from Command import CreateFileCommand


def main():
    # Initialize file storage
    storage = FileStorage()

    # Creating a folder
    create_folder_cmd = CreateFolderCommand(storage, "/", "Documents")
    create_folder_cmd.execute()

    # Creating a file
    create_file_cmd = CreateFileCommand(storage, "/Documents", "file1.txt", "Hello World")
    create_file_cmd.execute()

    # encrypt the file using Decorator
    file = storage.get_file("/Documents/file1.txt")
    encrypted_file = EncryptedFile(file)

    # Uploading to the encrypted file
    upload_cmd = UpdateCommand(file, "Updated Content")
    upload_cmd.execute()

    # Uploading again to create another version
    upload_cmd2 = UpdateCommand(file, "Final Content")
    upload_cmd2.execute()

    # Sharing the encrypted file
    share_cmd = ShareCommand(encrypted_file, ["user1@example.com"], permission_type="write")
    share_cmd.execute()

    # Accessing file versions
    print("Current Data:", encrypted_file.get_data())
    print("Version 0 Data:", file.get_version(0))  # First version
    print("Version 1 Data:", file.get_version(1))  # Second version

    # Deleting the file
    delete_cmd = DeleteCommand(storage, "/Documents/file1.txt")
    delete_cmd.execute()

if __name__ == "__main__":
    main()

