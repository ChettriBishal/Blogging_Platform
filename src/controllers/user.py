from datetime import date


class User:
    def __init__(self, user_info):
        (
            self.user_id,
            self.registration_date,
            self.username,
            self.password,
            self.user_role,
            self.email,
        ) = user_info
        # db must contain these fields in this order only

    @classmethod
    def user_creation(cls, user_info):  # to create from nothing
        user_id = None  # put generate random uuid
        registration_date = date.today()
        complete_user_info = (user_id, registration_date) + user_info
        return cls(complete_user_info)

    def remove_user(self):
        pass

    def change_password(self):
        pass


class Admin(User):
    def get_users(self):
        pass


class Blogger(User):
    pass
