"""Module which allows user to register into the platform"""

from typing import Tuple, Any

from models.user.user_model import User
from config.flags import Flag
from utils import validation
from utils.exceptions import AlreadyExists
from handlers.authentication.user.user_signup_handler import UserSignUpHandler
from config.message import Message


class UserSignUp:
    """
    Class allowing user to signup as a user into the platform
    """

    @staticmethod
    def sign_up(*user_info: Tuple) -> tuple[dict[str, Any], int] | Any:
        """Method which allows a user to register to the system
        """
        try:
            register_obj = UserSignUpHandler(user_info)
            user_id = register_obj.register_user()
            return {"userId": user_id, "message": Message.BLOGGER_REGISTERED}, 201
        except AlreadyExists as exc:
            return exc.dump()
