"""Module which allows user to register into the platform"""

from datetime import datetime
from typing import Tuple, Union

from controllers.user import User
from config.roles import Role
from config.flags import Flag
from utils import validation

from handlers.authentication.user.user_signup_handler import UserSignUpHandler


class UserSignUp:
    """
    Class allowing user to signup as a user into the platform
    """

    @staticmethod
    def sign_up(*user_info: Tuple) -> Union[User, bool, int]:
        """
        Method which allows a user to register to the system
        """
        username, password, email = user_info
        user_presence = UserSignUpHandler.check_user_presence(user_info)

        if user_presence:
            return Flag.ALREADY_EXISTS.value

        if not validation.validate_username(username):
            return Flag.INVALID_USERNAME.value

        if not validation.validate_password(password):
            return Flag.INVALID_PASSWORD.value

        if not validation.validate_email(email):
            return Flag.INVALID_EMAIL.value

        new_user = UserSignUpHandler.register_user(user_info)

        return new_user
