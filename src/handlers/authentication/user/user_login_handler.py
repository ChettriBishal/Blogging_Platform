from datetime import datetime
from typing import Union

from config.roles import Role
from config.flags import Flag
from utils import validation
from models.database import Database
from config.sql_query_mysql import Sql
from utils.authentication.hash_password_util import HashPassword
from utils.authentication.check_password_util import CheckPassword


class UserLoginHandler:
    @staticmethod
    def check_user_presence(userinfo) -> bool:
        print(Sql.GET_USER_BY_USERNAME.value)
        username_exists = Database.get_item(Sql.GET_USER_BY_USERNAME.value, (userinfo[0],))
        if username_exists:
            return True
        return False

    @staticmethod
    def authenticate_user(user_info) -> bool:
        username, password = user_info

        password_in_db = Database.get_item(Sql.GET_PASSWORD.value, (username,))[0]
        if CheckPassword.check_password(password, password_in_db):
            return True
        return False
