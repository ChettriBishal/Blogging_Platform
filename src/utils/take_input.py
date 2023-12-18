"""This module defines various methods to take user inputs"""

import pwinput
from typing import Tuple
from config import prompts
from utils import validation


def get_user_details() -> Tuple:
    """
    To get the username, password and email of the user
    """
    username = input(prompts.ENTER_USERNAME)
    passw = pwinput.pwinput(prompts.ENTER_PASSWORD, "*")
    email = input(prompts.ENTER_EMAIL)

    return username, passw, email


def get_username_password() -> Tuple:
    """
    To get the username and password of the user
    """
    username = input(prompts.ENTER_USERNAME)
    passw = pwinput.pwinput(prompts.ENTER_PASSWORD, "*")

    return username, passw


def get_new_password() -> str:
    """
    To get the new password from the user
    """
    passw = pwinput.pwinput(prompts.ENTER_NEW_PASSWORD, "*")

    return passw


def get_blog_post_details() -> Tuple:
    """
    To get the post details for creating a new blog
    """
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


def get_comment() -> str:
    """
    To get the comment content from the user
    """
    content = input(prompts.ENTER_COMMENT)

    if validation.validate_empty_input(content):
        print(prompts.EMPTY_INPUT)
        return get_comment()

    return content


def get_title() -> str:
    """
    To get the title for the blog from the user
    """
    title = input(prompts.ENTER_BLOG_TITLE)

    if validation.validate_empty_input(title):
        print(prompts.EMPTY_INPUT)
        return get_title()

    return title


def get_new_content() -> str:
    """
    To get new content for the post
    """
    content = input(prompts.ENTER_NEW_CONTENT)

    if validation.validate_empty_input(content):
        print(prompts.EMPTY_INPUT)
        return get_new_content()

    return content


def get_user_for_blog() -> str:
    """
    To get the username to search for blogs
    """
    username = input(prompts.ENTER_USERNAME_FOR_BLOGS)

    return username


def get_tag_name() -> str:
    """
    To get the tag name to search for blogs
    """
    tag_name = input(prompts.ENTER_TAG_FOR_BLOGS)

    if validation.validate_empty_input(tag_name):
        print(prompts.EMPTY_INPUT)
        return get_tag_name()

    return tag_name
