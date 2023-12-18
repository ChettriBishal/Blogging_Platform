"""This module contains various choices for the home menu"""

from config import prompts
from helpers.home import signup, signin


class Home:
    """
    Class containing the home menu which allows users to either signup or signin
    """

    @classmethod
    def home_menu(cls) -> None:
        choice = input(prompts.HOME_DISPLAY)
        if choice == '1':
            signup()
        elif choice == '2':
            signin()
        elif choice == '3':
            exit(0)
        else:
            print(prompts.ENTER_VALID_CHOICE)

        cls.home_menu()

