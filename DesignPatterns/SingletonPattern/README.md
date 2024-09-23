# Singleton Design Pattern

## Overview

The **Singleton Design Pattern** ensures that a class has only one instance and provides a global point of access to that instance. This pattern is useful when exactly one object is needed to coordinate actions across a system.

### Key Features:
1. **Single Instance:** Ensures only one instance of the class is created.
2. **Global Access Point:** Provides a single point of access to the instance.
3. **Thread-Safety:** Ensures the Singleton instance is accessed in a thread-safe manner (optional but recommended in multithreaded environments).

## Why Singleton?

Singletons are often used to manage resources that are expensive to create or need to be shared across the system, such as:
- Database connections
- Logging systems
- Configuration settings

## Implementation Example: `DatabaseConnection` Class

Below is an example from our codebase that demonstrates the Singleton pattern using a `DatabaseConnection` class. The class ensures that only one connection to the database is established, no matter how many times it is called. check the complete code in the repository.

### Code Example

```python
import threading

class DatabaseConnection:
    _instance = None  # Class variable to store the single instance of DatabaseConnection
    _lock = threading.Lock()  # Class-level lock for thread-safe singleton

    def __new__(cls):
        """
        This method controls the creation of a new instance in a thread-safe way.
        It ensures only one instance of the class is created.
        """
        if cls._instance is None:
            with cls._lock:  # Ensure thread safety by locking the resource
                if cls._instance is None:  # Double-checked locking
                    print("Creating new database connection...")
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize_connection()  # Initialize the database connection
        return cls._instance


