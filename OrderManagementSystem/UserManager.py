from UserFactory import UserFactory

class UserManager:
    """Manager for creating and handling users."""
    user_counter = 0

    def create_user(self, user_type, name):
        """Create a user using the UserFactory."""
        UserManager.user_counter+=1
        user_id = UserManager.user_counter

        return UserFactory.create_user(user_type, user_id, name)