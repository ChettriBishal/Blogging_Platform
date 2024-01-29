class UserResponse:
    """Receives user data from the database as it is"""

    def __init__(self, user_info):
        (
            self.user_id, self.username, self.password, self.user_role, self.email, self.registration_date
        ) = user_info

    def to_dict(self):
        """To return the user data in dictionary format"""
        return {
            "username": self.username,
            "user_role": self.user_role,
            "email": self.email,
            "registration_date": self.registration_date.strftime('%Y-%m-%d')
        }
