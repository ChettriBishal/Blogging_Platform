import hashlib
from datetime import datetime

from src.helpers import take_input, validation
from src.controllers import user
from src.common.roles import Role
from src.common.flags import Flag
from src.models import database
from src.common.sql_query import Sql


class Authentication:

    def hash_password(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def _check_password(self, password, hashed_password):
        if self.hash_password(password) == hashed_password:
            return True
        return False

    def sign_up(self):
        username, passw, email = take_input.get_user_details()

        user_presence = database.get_item(Sql.GET_USER_BY_USERNAME.value, (username,))

        if user_presence:
            return Flag.ALREADY_EXISTS.value

        if validation.validate_username(username) is None:
            return Flag.INVALID_USERNAME.value

        if validation.validate_password(passw) is None:
            return Flag.INVALID_PASSWORD.value

        if validation.validate_email(email) is None:
            return Flag.INVALID_EMAIL.value

        hashed_password = self.hash_password(passw)

        registration_date = datetime.today().strftime('%Y-%m-%d')
        new_user = user.User(username, hashed_password, Role.BLOGGER.value, email, registration_date)

        if new_user.add():
            return new_user
        else:
            return False

    def sign_in(self):
        username, passw = take_input.get_username_password()

        if validation.validate_username(username) is None:
            return Flag.INVALID_USERNAME.value

        user_presence = database.get_item(Sql.GET_USER_BY_USERNAME.value, (username,))

        if user_presence is None:
            return Flag.DOES_NOT_EXIST.value

        password_in_db = database.get_item(Sql.GET_PASSWORD.value, (username,))[0]

        if self._check_password(passw, password_in_db):
            return username
        else:
            return False


