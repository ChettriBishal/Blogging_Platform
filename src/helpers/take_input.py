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


def get_blog_post_details():
    pass


def get_comment_details():
    ...  # comment is not going to have title
    pass
