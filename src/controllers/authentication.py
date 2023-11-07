from datetime import datetime

from bcrypt import checkpw, hashpw, gensalt

from src.helpers import take_input
from src.controllers import user
from src.common.roles import Role


class Authentication:

    def _check_password(self, password, hashed_password):
        if checkpw(password.encode('utf8'), hashed_password):
            return True
        return False

    def _hash_password(self, password):
        salt = gensalt()
        hashed_password = hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def sign_up(self, user_details):
        username, passw, email = take_input.get_user_details()
        hashed_password = self._hash_password(passw)

        # create user object
        registration_date = datetime.today().strftime('%Y-%m-%d')
        new_user = user.User(username, hashed_password, Role.BLOGGER, registration_date)
        new_user.add()

    def sign_in(self):
        pass
