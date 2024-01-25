"""This module contains various methods that a user can perform"""

from config import prompts
from utils import take_input
from helpers.blogger import (view_blogs, view_one_blog, view_blogs_by_user, view_blogs_by_tag_name, create_blog,
                                 edit_blog, remove_blog, upvote_blog, comment_on_blog, change_password)


def blogger_menu(active_user) -> None:
    """
    To allow user to choose among various operations.
    :param active_user: User
    :return: None
    """
    menu_prompt = prompts.BLOGGER_MENU

    choice = input(menu_prompt)

    if choice == '1':
        view_blogs()
        blogger_menu(active_user)

    elif choice == '2':
        username = take_input.get_user_for_blog()
        view_blogs_by_user(username)
        blogger_menu(active_user)

    elif choice == '3':
        tag_name = take_input.get_tag_name()
        view_blogs_by_tag_name(tag_name)
        blogger_menu(active_user)

    elif choice == '4':
        view_one_blog()
        blogger_menu(active_user)

    elif choice == '5':
        create_blog(active_user)
        blogger_menu(active_user)

    elif choice == '6':
        edit_blog(active_user)
        blogger_menu(active_user)

    elif choice == '7':
        remove_blog(active_user)
        blogger_menu(active_user)

    elif choice == '8':
        upvote_blog(active_user)
        blogger_menu(active_user)

    elif choice == '9':
        comment_on_blog(active_user)
        blogger_menu(active_user)

    elif choice == '10':
        change_password(active_user)
        blogger_menu(active_user)

    elif choice == '11':
        pass

    else:
        print(prompts.ENTER_VALID_CHOICE)
        blogger_menu(active_user)


