from typing import Tuple

from config.flags import Flag
from utils import validation

from handlers.authentication.user.user_login_handler import UserLoginHandler


class UserLogin:
    """
    Class allowing user to login to the platform
    """

    @staticmethod
    def sign_in(*user_info: Tuple) -> bool:
        """
        Method to allow user entry to the system
        """
        username, password = user_info

        if validation.validate_username(username) is None:
            return Flag.INVALID_USERNAME.value

        user_presence = UserLoginHandler.check_user_presence(user_info)
        if not user_presence:
            return Flag.DOES_NOT_EXIST.value

        user_logged_in = UserLoginHandler.authenticate_user(user_info)

        return user_logged_in

