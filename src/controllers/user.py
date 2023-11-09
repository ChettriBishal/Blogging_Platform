from datetime import date

from src.common.sql_query import SQL
from src.models import database


class User:
    def __init__(self, *user_info):
        (
            # receive user_id from the database itself
            self.username,
            self.password,
            self.user_role,
            self.email,
            self.registration_date,
        ) = user_info

        self.user_info = user_info
        # db must contain these fields in this order only

    def get_details(self):
        return {
            'username': self.username,
            'role': self.user_role,
            'email': self.email,
            'registration_date': self.registration_date,
        }

    def add(self):
        # adding this user object to db
        try:
            database.insert_item(SQL['INSERT_USER'].value, self.user_info)
            return True
        except Exception as exc:
            print(exc)
            return False

    def remove_user_by_username(self):
        try:
            database.remove_item(SQL['REMOVE_USER'].value, self.username)
            return True
        except Exception as exc:
            print(exc)
            return False

    def change_password(self, new_password):
        try:
            database.insert_item(SQL['UPDATE_PASSWORD'].value, (new_password, self.username))
            return True
        except Exception as exc:
            print(exc)
            return False


class Admin(User):
    def get_users(self):
        pass


class Blogger(User):
    pass
