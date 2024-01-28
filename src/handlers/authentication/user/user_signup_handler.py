from datetime import datetime
from typing import Union

from models.user import User
from config.roles import Role
from models.database import Database
from config.sql_query_mysql import Sql
from utils.authentication.hash_password_util import HashPassword


class UserSignUpHandler:
    @staticmethod
    def check_user_presence(user_info) -> bool:
        """This checks if user by username or/email is already present in the platform"""
        username, _, email = user_info
        username_exists = Database.get_item(Sql.GET_USER_BY_USERNAME.value, (username,))
        email_exists = Database.get_item(Sql.GET_USER_BY_EMAIL.value, (email,))

        if username_exists or email_exists:
            return True
        return False

    @staticmethod
    def register_user(user_info) -> Union[User, None]:
        """This creates a user object which interacts with the database"""
        username, password, email = user_info
        hashed_password = HashPassword.hash_password(password)
        registration_date = datetime.today().strftime('%Y-%m-%d')
        new_user = User(username, hashed_password, Role.BLOGGER.value, email, registration_date)

        if new_user.add():
            return new_user
        else:
            return None
