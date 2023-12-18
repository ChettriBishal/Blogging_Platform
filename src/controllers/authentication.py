"""Module which contains the logic for authenticating a user and allowing access to the system"""

import hashlib
from datetime import datetime
from typing import Tuple, Union

from controllers.user import User
from config.roles import Role
from config.flags import Flag
from utils import validation
from models.database import Database
from config.sql_query import Sql


class Authentication:
    """
    Class containing various methods for authenticating a user to the system
    """

    @classmethod
    def hash_password(cls, password: str) -> str:
        """
        Method for hashing the password entered by the user
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    @classmethod
    def _check_password(cls, password: str, hashed_password: str) -> bool:
        """
        Method for validating the password against the stored password
        """
        if cls.hash_password(password) == hashed_password:
            return True
        return False

    @classmethod
    def sign_up(cls, *user_info: Tuple) -> Union[User, bool, int]:
        """
        Method which allows a user to register to the system
        """
        username, passw, email = user_info

        user_presence = Database.get_item(Sql.GET_USER_BY_USERNAME.value, (username,))

        if user_presence:
            return Flag.ALREADY_EXISTS.value

        if not validation.validate_username(username):
            return Flag.INVALID_USERNAME.value

        if not validation.validate_password(passw):
            return Flag.INVALID_PASSWORD.value

        if not validation.validate_email(email):
            return Flag.INVALID_EMAIL.value

        hashed_password = cls.hash_password(passw)

        registration_date = datetime.today().strftime('%Y-%m-%d')
        new_user = User(username, hashed_password, Role.BLOGGER.value, email, registration_date)

        if new_user.add():
            return new_user
        else:
            return False

    @classmethod
    def sign_in(cls, *args: Tuple) -> Union[tuple, bool, str]:
        """
        Method to allow user entry to the system
        """
        username, passw = args

        if validation.validate_username(username) is None:
            return Flag.INVALID_USERNAME.value

        user_presence = Database.get_item(Sql.GET_USER_BY_USERNAME.value, (username,))

        if user_presence is None:
            return Flag.DOES_NOT_EXIST.value

        password_in_db = Database.get_item(Sql.GET_PASSWORD.value, (username,))[0]

        if cls._check_password(passw, password_in_db):
            return username
        else:
            return False
