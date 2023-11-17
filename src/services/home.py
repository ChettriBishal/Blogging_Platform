from src.common import prompts
from src.common.sql_query import Sql
from src.controllers.authentication import Authentication
from src.controllers.user import User
from src.common.flags import Flag
from src.common.roles import Role
from src.models import database
from src.services import blogger
from src.loggers.general_logger import GeneralLogger
from src.common import filepaths


def home_menu():
    choice = input(prompts.HOME_DISPLAY)

    if choice == '1':
        signup()
        home_menu()

    elif choice == '2':
        signin()
        home_menu()

    elif choice == '3':
        exit(0)

    else:
        print(prompts.ENTER_VALID_CHOICE)
        home_menu()


def signup():
    print(prompts.SIGNUP)

    auth = Authentication()
    new_user = auth.sign_up()

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
        home_menu()

    else:
        print(prompts.PLEASE_TRY_AGAIN)
        signup()


def signin():
    print(prompts.SIGNIN)

    auth = Authentication()
    user_logging_in = auth.sign_in()

    if user_logging_in == Flag.INVALID_USERNAME.value:
        print(prompts.ENTER_VALID_USERNAME)
        signin()

    elif user_logging_in == Flag.DOES_NOT_EXIST.value:
        print(prompts.USER_DOES_NOT_EXIST)
        signin()

    elif user_logging_in:
        print(prompts.USER_LOGGED_IN.format(user_logging_in))
        GeneralLogger.info(prompts.USER_LOGGED_IN.format(user_logging_in), filepaths.USER_LOG_FILE)

        record = database.get_item(Sql.GET_USER_BY_USERNAME.value, (user_logging_in,))

        user_logged_in = User(*record[1:])
        user_logged_in.set_user_id(record[0])

        user_logged_in.user_role = int(user_logged_in.user_role)

        if user_logged_in.user_role == Role.ADMIN.value:
            blogger.admin_menu(user_logged_in)

        elif user_logged_in.user_role == Role.BLOGGER.value:
            blogger.blogger_menu(user_logged_in)

    else:
        print(prompts.WRONG_PASSWORD)
        signin()
