import hashlib
from datetime import datetime

from src.controllers import user
from src.common.roles import Role
from src.common.flags import Flag
from src.utils import take_input, validation
from src.controllers.database import Database
from src.common.sql_query import Sql


class Authentication:

    @classmethod
    def hash_password(cls, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    @classmethod
    def _check_password(cls, password, hashed_password):
        if cls.hash_password(password) == hashed_password:
            return True
        return False

    @classmethod
    def sign_up(cls):
        username, passw, email = take_input.get_user_details()

        user_presence = Database.get_item(Sql.GET_USER_BY_USERNAME.value, (username,))

        if user_presence:
            return Flag.ALREADY_EXISTS.value

        if validation.validate_username(username) is None:
            return Flag.INVALID_USERNAME.value

        if validation.validate_password(passw) is None:
            return Flag.INVALID_PASSWORD.value

        if validation.validate_email(email) is None:
            return Flag.INVALID_EMAIL.value

        hashed_password = cls.hash_password(passw)

        registration_date = datetime.today().strftime('%Y-%m-%d')
        new_user = user.User(username, hashed_password, Role.BLOGGER.value, email, registration_date)

        if new_user.add():
            return new_user
        else:
            return False

    @classmethod
    def sign_in(cls):
        username, passw = take_input.get_username_password()

        if validation.validate_username(username) is None:
            return Flag.INVALID_USERNAME.value

        user_presence = Database.get_item(Sql.GET_USER_BY_USERNAME.value, (username,))

        if user_presence is None:
            return Flag.DOES_NOT_EXIST.value

        password_in_db = Database.get_item(Sql.GET_PASSWORD.value, (username,))[0]

        if cls._check_password(passw, password_in_db):
            return username
        else:
            return False


