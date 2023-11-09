import hashlib
from datetime import datetime

from src.helpers import take_input, validation
from src.controllers import user
from src.common.roles import Role

from src.models import database
from src.common.sql_query import SQL


class Authentication:

    def _hash_password(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def _check_password(self, password, hashed_password):
        if self._hash_password(password) == hashed_password:
            return True
        return False

    def sign_up(self):
        username, passw, email = take_input.get_user_details()
        if validation.validate_username(username) is None:
            return -1  # will return -1 for invalid username and password

        if validation.validate_password(passw) is None:
            return -1

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

        # before getting the password check if user exists
        user_presence = database.query_with_params(SQL.GET_USER_BY_USERNAME, (username,))

        if user_presence is None:
            return -1
            # -1 denotes that user does not exist

        password_in_db = database.get_item(SQL.GET_PASSWORD.value, (username,))[0]

        if validation.validate_username(username) is None:
            return -1

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
