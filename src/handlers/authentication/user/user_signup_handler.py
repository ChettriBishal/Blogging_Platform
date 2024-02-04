from datetime import datetime
from typing import Union, Tuple

from models.user.user_model import User
from config.roles import Role
from models.database import Database
from config.sql_query_mysql import Sql
from utils.authentication.hash_password_util import HashPassword
from utils.exceptions import DbException, AlreadyExists
from config.message import Message


class UserSignUpHandler:
    def __init__(self, user_info: Tuple):
        self.user_info = user_info

    def check_user_presence(self) -> bool:
        """This checks if user by username or/email is already present in the platform"""
        try:
            username, _, email = self.user_info
            username_exists = Database.get_item(Sql.GET_USER_BY_USERNAME.value, (username,))
            email_exists = Database.get_item(Sql.GET_USER_BY_EMAIL.value, (email,))

            if username_exists or email_exists:
                return True
            return False
        except DbException:
            raise DbException(code=500, message=Message.INTERNAL_SERVER_ERROR)

    def register_user(self) -> Union[User, None]:
        """This creates a user object which interacts with the database"""
        try:
            if self.check_user_presence():
                raise AlreadyExists(code=409, message=Message.USER_ALREADY_EXISTS)

            username, password, email = self.user_info
            hashed_password = HashPassword.hash_password(password)
            registration_date = datetime.today().strftime('%Y-%m-%d')
            new_user = User(username, hashed_password, Role.BLOGGER.value, email, registration_date)

            new_user.add()
            return new_user
        except DbException:
            raise DbException
