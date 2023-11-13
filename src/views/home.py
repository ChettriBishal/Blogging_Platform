from src.common import prompts
from src.common.sql_query import Sql
from src.controllers.authentication import Authentication
from src.controllers.user import User
from src.common.flags import Flag
from src.common.roles import Role

from src.models import database

from src.views import blogger


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
        print("Enter a valid choice!")


def signup():
    print("---------------SIGN UP---------------")
    auth = Authentication()
    new_user = auth.sign_up()
    if new_user == -1:
        print("Invalid username")
        signup()
    elif new_user == Flag.INVALID_PASSWORD.value:
        print("Invalid password")
        signup()
    elif new_user == Flag.INVALID_EMAIL.value:
        print("Invalid email")
        signup()
    elif new_user:
        print("User signed up successfully!!")
        print(new_user.get_details())
    else:
        print("Try again")
        signup()


def signin():
    print("---------------SIGN IN---------------")
    auth = Authentication()
    user_logging_in = auth.sign_in()
    if user_logging_in == Flag.INVALID_USERNAME.value:
        print("Enter a valid username")
        signin()
    elif user_logging_in == Flag.DOES_NOT_EXIST.value:
        print("This user does not exist")
        signin()
    elif user_logging_in:
        # firstly create a user object,
        # then show menus on the basis of roles
        print("User logged successfully!!!")
        record = database.get_item(Sql.GET_USER_BY_USERNAME.value, (user_logging_in,))

        user_logged_in = User(*record[1:])
        user_logged_in.set_user_id(record[0])
        print(user_logged_in.get_details())

        print(f"User role for {user_logging_in} -> {user_logged_in.user_role}")

        user_logged_in.user_role = int(user_logged_in.user_role)

        if user_logged_in.user_role == Role.ADMIN.value:
            pass
            # menu for blogger operations
        elif user_logged_in.user_role == Role.BLOGGER.value:
            blogger.blogger_menu(user_logged_in)
            # menu for admin operations
        print(user_logged_in)

    else:
        print("Wrong password! Please try again!")
        signin()
