from datetime import date

from src.common.sql_query import SQL

class User:
    def __init__(self, user_info):
        (
            # receive user_id from the database itself
            self.username,
            self.password,
            self.user_role,
            self.email,
            self.registration_date,
        ) = user_info
        # db must contain these fields in this order only

    def add(self):
        # adding this user object to db
        try:


        except Exception as exc:
            print(exc)



    def remove_user(self):
        pass

    def change_password(self):
        pass


class Admin(User):
    def get_users(self):
        pass


class Blogger(User):
    pass
