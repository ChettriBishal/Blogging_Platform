from typing import Tuple, Dict, Any

from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required
from models.database import Database
from config.sql_query_mysql import Sql
from utils.authentication.check_password_util import CheckPassword
from utils.exceptions import DbException, DoesNotExist, WrongCredentials
from config.message import Message


class UserLoginHandler:
    def __init__(self, userinfo):
        self.userinfo = userinfo
        self.username = userinfo[0]
        self._password = userinfo[1]

    def check_user_presence(self) -> bool:
        """To check if user exists in database"""
        try:
            username_exists = Database.get_item(Sql.GET_USER_BY_USERNAME.value, (self.userinfo[0],))
            if username_exists:
                return True
            return False
        except DbException:
            raise DbException

    def authenticate_user(self) -> bool:
        """To validate user info as entered against the database"""
        try:
            username, password = self.userinfo
            password_in_db = Database.get_item(Sql.GET_PASSWORD.value, (username,))[0]

            if CheckPassword.check_password(password, password_in_db):
                return True
            return False
        except DbException:
            raise DbException

    def user_login(self) -> tuple[dict[str, Any], int]:
        """To perform login operation into the platform"""
        try:
            user_presence = self.check_user_presence()
            if not user_presence:
                raise DoesNotExist(code=404, message=Message.USER_NOT_FOUND)

            user_logged_in = self.authenticate_user()

            if user_logged_in:
                user_additional_claims = {"username": self.username}
                access_token = create_access_token(identity=self.username, fresh=True,
                                                   additional_claims=user_additional_claims)
                refresh_token = create_refresh_token(identity=self.username,
                                                     additional_claims=user_additional_claims)

                return {"access_token": access_token, "refresh_token": refresh_token}, 200
            else:
                raise WrongCredentials(code=401, message=Message.WRONG_CREDENTIALS)


        except DbException:
            raise DbException
