"""This module contains the menu choices for admin"""

from config import prompts
from config.flags import Flag
from views.blogger import blogger_menu
from helpers.blogger import (admin_remove_blog,
                                 get_users, display_users, remove_user_by_username, change_password)


def admin_choice_menu(active_user) -> None:
    """
    To allow admin to choose his login method
    :param active_user: User
    :return: None
    """
    choice = input(prompts.ADMIN_CHOICE_PROMPT)
    if choice == '1':
        admin_menu(active_user)
        admin_choice_menu(active_user)
    elif choice == '2':
        blogger_menu(active_user)
        admin_choice_menu(active_user)
    elif choice == '3':
        pass
    else:
        print(prompts.ENTER_VALID_CHOICE)
        admin_choice_menu(active_user)


def admin_menu(active_user) -> None:
    """
    To allow admin to choose various operations
    :param active_user: User
    :return: None
    """
    menu_prompt = prompts.ADMIN_SPECIFIC

    choice = input(menu_prompt)

    if choice == '1':
        admin_remove_blog(active_user)
        admin_menu(active_user)

    elif choice == '2':
        users = get_users(active_user)
        users = [dict(user.get_details()) for user in users]

        display_users(users)
        admin_menu(active_user)

    elif choice == '3':
        user_to_remove = input(prompts.ENTER_USERNAME_TO_REMOVE)

        status = remove_user_by_username(user_to_remove)

        if status == Flag.INVALID_OPERATION.value:
            pass
        elif status:
            print(prompts.USER_REMOVED)
        else:
            print(prompts.USER_DOES_NOT_EXIST)

        admin_menu(active_user)

    elif choice == '4':
        change_password(active_user)
        admin_menu(active_user)

    elif choice == '5':
        pass

    else:
        print(prompts.ENTER_VALID_CHOICE)
        admin_menu(active_user)
