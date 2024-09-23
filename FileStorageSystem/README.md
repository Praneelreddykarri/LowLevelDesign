# Google Drive File Storage System

## Overview
This File Storage System simulates features similar to cloud storage services like Google Drive. It supports file creation, uploading, sharing, versioning, and access control, with added encryption for security.

## Requirements
To implement a low-level design for a file storage system, the following features are needed:

- **File/Folder Creation**: Ability to create files and folders within the storage.
- **File Uploading**: Users can upload new data to existing files.
- **File Sharing**: Files can be shared with users, along with permission management.
- **File Versioning**: Track and retrieve different versions of files.
- **Access Control and Permissions**: Manage user permissions for accessing files.

## Design Patterns Used

1. **Command Pattern**
   - Used for encapsulating all file operations (e.g., uploading, sharing, deleting) as commands.
   - Allows for easy extension and modification of commands without changing existing code.

2. **Decorator Pattern**
   - Implemented in the `EncryptedFile` class to add encryption functionality to the base `File` class.
   - This allows for the dynamic addition of responsibilities to individual file instances.

3. **Singleton Pattern**
   - Implemented in the `FileStorage` class to ensure that only one instance of the storage exists throughout the application.
   - This prevents conflicts and ensures consistent access to the storage.

## SOLID Principles Used

1. **Single Responsibility Principle (SRP)**
   - Each class has a single responsibility. For example, the `File` class manages file data, while the `Permissions` class handles user permissions.

2. **Open/Closed Principle (OCP)**
   - The system is open for extension but closed for modification. New command classes can be added without modifying existing classes.

3. **Liskov Substitution Principle (LSP)**
   - Subtypes can be substituted for their base types. The `EncryptedFile` can be used in place of a `File` without altering the desired behavior.

4. **Interface Segregation Principle (ISP)**
   - Interfaces are designed to be client-specific. Each command implements the `Command` interface, focusing only on its particular operation.

5. **Dependency Inversion Principle (DIP)**
   - High-level modules do not depend on low-level modules. For example, the command execution does not rely on the specific implementation of the file but rather on the abstract command interface.


