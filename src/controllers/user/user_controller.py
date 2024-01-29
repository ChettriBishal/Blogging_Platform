from typing import Union, List, Dict
from models.user.user_model import User
from models.database import Database
from config.sql_query_mysql import Sql
from config import filepaths
from utils.authentication.hash_password_util import HashPassword
from utils import validation
from loggers.general_logger import GeneralLogger
from models.user.user_response_model import UserResponse
from utils.users.get_current_user import GetCurrentUser
from handlers.user.user_info_handler import UserInfoHandler


class UserController:
    """This will help with user related operations"""

    def get_self_details(self) -> Dict:
        username = GetCurrentUser.get_user_name()
        user_details = UserInfoHandler.get_user_row_by_username(username)
        user_obj = UserResponse(user_details)
        return user_obj.to_dict()

    def get_all_users(self):
        # put rbac for admin here
        """
        To get all the users in the platform
        """
        try:
            user_list = Database.get_items(Sql.GET_ALL_USERS.value)
            users = [User(*record[1:]) for record in user_list]

            return users

        except PermissionError as permission_exc:
            GeneralLogger.info(permission_exc, filepaths.USER_LOG_FILE)

    def remove_user_by_username(self):
        pass

    def change_password(active_user: User) -> None:
        """
        To change the password: performed by the active user
        """
        new_passw = take_input.get_new_password()

        if validation.validate_password(new_passw):
            hashed_passw = HashPassword.hash_password(new_passw)

            if active_user.change_password(hashed_passw):
                print(prompts.SUCCESSFUL_PASSWORD_CHANGE)
                GeneralLogger.info(prompts.USER_CHANGED_PASSWORD.format(active_user.username), filepaths.USER_LOG_FILE)

        else:
            print(prompts.ENTER_STRONG_PASSWORD)
            change_password(active_user)
