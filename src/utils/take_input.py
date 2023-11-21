import pwinput
from src.config import prompts
from src.utils import validation


def get_user_details():
    username = input(prompts.ENTER_USERNAME)
    passw = pwinput.pwinput(prompts.ENTER_PASSWORD, "*")
    email = input(prompts.ENTER_EMAIL)

    return username, passw, email


def get_username_password():
    username = input(prompts.ENTER_USERNAME)
    passw = pwinput.pwinput(prompts.ENTER_PASSWORD, "*")

    return username, passw


def get_new_password():
    passw = pwinput.pwinput(prompts.ENTER_NEW_PASSWORD, "*")

    return passw


def get_blog_post_details():
    title = input(prompts.ENTER_BLOG_TITLE)

    if validation.validate_empty_input(title):
        print(prompts.EMPTY_INPUT)
        return get_blog_post_details()

    content = input(prompts.ENTER_BLOG_CONTENT)

    if validation.validate_empty_input(content):
        print(prompts.EMPTY_INPUT)
        return get_blog_post_details()

    tag = input(prompts.ENTER_BLOG_TAG)

    if validation.validate_empty_input(tag):
        print(prompts.EMPTY_INPUT)
        return get_blog_post_details()

    return title, content, tag


def get_comment():
    content = input(prompts.ENTER_COMMENT)

    if validation.validate_empty_input(content):
        print(prompts.EMPTY_INPUT)
        return get_comment()

    return content


def get_title():
    title = input(prompts.ENTER_BLOG_TITLE)

    if validation.validate_empty_input(title):
        print(prompts.EMPTY_INPUT)
        return get_title()

    return title


def get_new_content():
    content = input(prompts.ENTER_NEW_CONTENT)

    if validation.validate_empty_input(content):
        print(prompts.EMPTY_INPUT)
        return get_new_content()

    return content


def get_user_for_blog():
    username = input(prompts.ENTER_USERNAME_FOR_BLOGS)

    return username


def get_tag_name():
    tag_name = input(prompts.ENTER_TAG_FOR_BLOGS)

    if validation.validate_empty_input(tag_name):
        print(prompts.EMPTY_INPUT)
        return get_tag_name()

    return tag_name
