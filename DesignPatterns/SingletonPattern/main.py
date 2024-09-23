from DatabaseConnection import DatabaseConnection

def main():
    # Attempt to create multiple database connections
    print("Initializing the first database connection:")
    db1 = DatabaseConnection()
    print(f"DB1 Connection: {db1.get_connection()}")

    print("\nAttempting to initialize a second database connection:")
    db2 = DatabaseConnection()
    print(f"DB2 Connection: {db2.get_connection()}")

    # Check if both instances are the same
    print("\nAre both connections the same instance?")
    print(db1 is db2)

if __name__ == "__main__":
    main()
