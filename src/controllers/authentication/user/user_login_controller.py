from typing import Tuple, Dict, Union
from handlers.authentication.user.user_login_handler import UserLoginHandler
from utils.exceptions import DbException, WrongCredentials, DoesNotExist


class UserLogin:
    """
    Class allowing user to login to the platform
    """

    @staticmethod
    def sign_in(*user_info: Tuple):
        """
        Method to allow user entry to the system
        """
        try:
            user_logged_in = UserLoginHandler(user_info)
            return user_logged_in.user_login()

        except DbException as exc:
            return {"code": exc.code, "message": exc.message}, exc.code

        except WrongCredentials as exc:
            return {"message": exc.message}, exc.code

        except DoesNotExist as exc:
            return {"message": exc.message}, exc.code

