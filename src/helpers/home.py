"""This module helps the user to enter to the platform"""

from config import prompts
from config.sql_query_mysql import Sql
from controllers.authentication import Authentication
from models.user import User
from config.flags import Flag
from config.roles import Role
from models.database import Database
from loggers.general_logger import GeneralLogger
from config import filepaths
from utils import take_input
from views.admin import admin_choice_menu
from views.blogger import blogger_menu


def signup() -> None:
    """
    This function allows users to sign up to the platform
    """
    print(prompts.SIGNUP)

    user_details = take_input.get_user_details()

    new_user = Authentication.sign_up(*user_details)

    if new_user == Flag.INVALID_USERNAME.value:
        print(prompts.ENTER_VALID_USERNAME)
        signup()

    elif new_user == Flag.ALREADY_EXISTS.value:
        print(prompts.USERNAME_ALREADY_EXISTS)
        signup()

    elif new_user == Flag.INVALID_PASSWORD.value:
        print(prompts.ENTER_STRONG_PASSWORD)
        signup()

    elif new_user == Flag.INVALID_EMAIL.value:
        print(prompts.ENTER_VALID_EMAIL)
        signup()

    elif new_user:
        print(prompts.USER_SIGNED_UP.format(new_user.username))
        GeneralLogger.info(prompts.USER_SIGNED_UP.format(new_user.username), filepaths.USER_LOG_FILE)

    else:
        print(prompts.PLEASE_TRY_AGAIN)


def signin() -> None:
    """
    This function allows users to sign in to the platform
    """
    print(prompts.SIGNIN)

    user_details = take_input.get_username_password()

    user_logging_in = Authentication.sign_in(*user_details)

    if user_logging_in == Flag.INVALID_USERNAME.value:
        print(prompts.ENTER_VALID_USERNAME)
        signin()

    elif user_logging_in == Flag.DOES_NOT_EXIST.value:
        print(prompts.USER_DOES_NOT_EXIST)
        signin()

    elif user_logging_in:
        print(prompts.USER_LOGGED_IN.format(user_logging_in))
        GeneralLogger.info(prompts.USER_LOGGED_IN.format(user_logging_in), filepaths.USER_LOG_FILE)

        record = Database.get_item(Sql.GET_USER_BY_USERNAME.value, (user_logging_in,))

        user_logged_in = User(*record[1:])
        user_logged_in.set_user_id(record[0])

        user_logged_in.user_role = int(user_logged_in.user_role)

        if user_logged_in.user_role == Role.ADMIN.value:
            admin_choice_menu(user_logged_in)

        elif user_logged_in.user_role == Role.BLOGGER.value:
            blogger_menu(user_logged_in)

    else:
        print(prompts.WRONG_PASSWORD)
        signin()
