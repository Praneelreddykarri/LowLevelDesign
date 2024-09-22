from User import VipUser, RegularUser

class UserFactory:
    @staticmethod
    def create_user(user_type, user_id, name):
        """Create a user based on the user type."""
        if user_type == "vip":
            return VipUser(user_id, name)
        elif user_type == "regular":
            return RegularUser(user_id, name)
        else:
            raise ValueError("Unknown user type")