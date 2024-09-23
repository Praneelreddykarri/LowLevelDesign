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

    def _initialize_connection(self):
        """This method simulates setting up a connection to a database."""
        self.connection = "Connected to the database"
        print("Database connection initialized.")

    def get_connection(self):
        """Returns the current database connection."""
        return self.connection

# You can now import DatabaseConnection and use it in other files.
