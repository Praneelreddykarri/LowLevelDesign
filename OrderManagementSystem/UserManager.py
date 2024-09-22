from UserFactory import UserFactory

class UserManager:
    """Manager for creating and handling users."""
    user_counter = 0

    def __init__(self):
        self.users = []  # List to store active orders

    @classmethod
    def generate_user_id(cls):
        """Thread-safe order ID generation."""
        with cls._lock:
            cls.user_counter += 1
            return cls.user_counter

    def create_user(self, user_type, name):
        """Create a user using the UserFactory."""
        user_id = self.generate_user_id()
        user = UserFactory.create_user(user_type, user_id, name)
        self.users.append(user)
        return user

    def print_all_users(self):
        for user in self.users:
            print("User Details", end="\n\n")
            print(f"User ID: {user.user_id}", end="\n\n")
            print(f"User Name: {user.name}", end="\n\n")
            print(f"User Type: {user.user_type}", end="\n\n")