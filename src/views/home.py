from src.config import prompts
from src.services.home import signup, signin


class Home:
    options = {'1': signup, '2': signin}

    @classmethod
    def home_menu(cls):
        choice = input(prompts.HOME_DISPLAY)
        choice_func = cls.options.get(choice)
        if choice == '3':
            exit(0)
        if cls.options.get(choice):
            choice_func()
        else:
            print(prompts.ENTER_VALID_CHOICE)

        cls.home_menu()

