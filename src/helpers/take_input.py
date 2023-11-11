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
    title = input(prompts.ENTER_BLOG_TITLE)
    content = input(prompts.ENTER_BLOG_CONTENT)
    tag = input(prompts.ENTER_BLOG_TAG)
    return title, content, tag


def get_comment():
    content = input(prompts.ENTER_COMMENT)
    return content
