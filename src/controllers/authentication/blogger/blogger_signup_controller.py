"""Module which allows user to register into the platform"""

from datetime import datetime
from typing import Tuple, Union

from controllers.user import User
from config.roles import Role
from config.flags import Flag
from utils import validation
from models.database import Database
from config.sql_query_mysql import Sql
from utils.authentication.hash_password_util import HashPassword


class BloggerSignUp:
    """
    Class allowing user to signup as a blogger into the platform
    """

    @classmethod
    def sign_up(cls, *user_info: Tuple) -> Union[User, bool, int]:
        """
        Method which allows a user to register to the system
        """
        username, passw, email = user_info

        user_presence = Database.get_item(Sql.GET_USER_BY_USERNAME.value, (username,))

        if user_presence:
            return Flag.ALREADY_EXISTS.value

        # if not validation.validate_username(username):
        #     return Flag.INVALID_USERNAME.value
        #
        # if not validation.validate_password(passw):
        #     return Flag.INVALID_PASSWORD.value
        #
        # if not validation.validate_email(email):
        #     return Flag.INVALID_EMAIL.value

        hashed_password = HashPassword.hash_password(passw)
        registration_date = datetime.today().strftime('%Y-%m-%d')
        new_user = User(username, hashed_password, Role.BLOGGER.value, email, registration_date)
        if new_user.add():
            return new_user
        else:
            return False
