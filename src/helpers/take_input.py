from src.common import prompts


def get_user_details():
    username = input(prompts.ENTER_USERNAME)
    passw = input(prompts.ENTER_PASSWORD)
    email = input(prompts.ENTER_EMAIL)
    return username, passw, email


def get_username_password():
    username = input(prompts.ENTER_USERNAME)
    passw = input(prompts.ENTER_PASSWORD)
    return username, passw
