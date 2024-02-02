from typing import Union, List, Dict
from models.user.user_model import User
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
        """
        To get all the users in the platform
        """
        try:
            user_list = UserInfoHandler.get_all_users()
            users = [UserResponse(record).to_dict() for record in user_list]
            return users

        except PermissionError as permission_exc:
            GeneralLogger.info(permission_exc, filepaths.USER_LOG_FILE)

    def get_user_details_by_username(self, username) -> Dict:
        """Get user details by username"""
        user_info = UserInfoHandler.get_user_row_by_username(username)
        return UserResponse(user_info).to_dict()

    def get_user_details_by_userid(self, userid) -> Dict:
        """Get user details by user ID"""
        username = UserInfoHandler.get_username_by_userid(userid)
        userinfo = self.get_user_details_by_username(username[0])
        return userinfo

    def remove_user_by_username(self):
        """To remove user by username -> only performed by admins"""
        pass

    def change_password(active_user: User) -> None:
        """
        To change the password: performed by the active user
        """
        pass
