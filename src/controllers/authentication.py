from datetime import datetime

from bcrypt import checkpw, hashpw, gensalt

from src.helpers import take_input
from src.controllers import user
from src.common.roles import Role

from src.models import database
from src.common.sql_query import SQL


class Authentication:

    def _check_password(self, password, hashed_password):
        if checkpw(password.encode('utf8'), hashed_password):
            return True
        return False

    def _hash_password(self, password):
        salt = gensalt()
        hashed_password = hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def sign_up(self):
        username, passw, email = take_input.get_user_details()
        hashed_password = self._hash_password(passw)

        # create user object
        registration_date = datetime.today().strftime('%Y-%m-%d')
        new_user = user.User(username, hashed_password, Role['BLOGGER'].value, email, registration_date)
        if new_user.add():
            return new_user
        else:
            return False

    def sign_in(self):
        username, passw = take_input.get_username_password()
        password_in_db = database.get_item(SQL['GET_PASSWORD'].value, (username,))

        if self._check_password(passw, password_in_db):
            return True
        else:
            return False


if __name__ == "__main__":
    auth = Authentication()
    # usr = auth.sign_up()
    # if usr:
    #     print("User signed up successfully!!")
    #     print(usr.get_details())
    # else:
    #     print("Try again")
    #     auth.sign_up()
    if auth.sign_in():
        print("User signed in successfully!!")
    else:
        print("Try again")
        auth.sign_in()
