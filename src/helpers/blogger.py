"""This module defines the various operations that a user can perform"""

from datetime import datetime
from prettytable import PrettyTable
from typing import List, Union

from config import prompts
from utils.admin_only import admin
from controllers.blog import Blog
from controllers.comment import Comment
from config.sql_query_mysql import Sql
from controllers.authentication import Authentication
from controllers.user import User
from config.flags import Flag
from config.roles import Role
from utils import take_input, validation
from models.database import Database
from loggers.general_logger import GeneralLogger
from config import filepaths


@admin
def get_users(active_user: User) -> Union[List[User], None]:
    """
    To get all the users in the platform
    """
    try:
        user_list = Database.get_items(Sql.GET_ALL_USERS.value)
        users = [User(*record[1:]) for record in user_list]

        return users

    except PermissionError as permission_exc:
        GeneralLogger.info(permission_exc, filepaths.USER_LOG_FILE)


def change_password(active_user: User) -> None:
    """
    To change the password: performed by the active user
    """
    new_passw = take_input.get_new_password()

    if validation.validate_password(new_passw):
        hashed_passw = Authentication.hash_password(new_passw)

        if active_user.change_password(hashed_passw):
            print(prompts.SUCCESSFUL_PASSWORD_CHANGE)
            GeneralLogger.info(prompts.USER_CHANGED_PASSWORD.format(active_user.username), filepaths.USER_LOG_FILE)

    else:
        print(prompts.ENTER_STRONG_PASSWORD)
        change_password(active_user)


def display_users(user_list: List) -> None:
    """
    To display the users of the platform
    """
    print(prompts.USERS_HEADER)
    table = PrettyTable()

    table.field_names = ["Username", "Role", "Email"]

    for person in user_list:
        role = int(person.get('role'))

        if role == Role.ADMIN.value:
            role = 'ADMIN'

        elif role == Role.BLOGGER.value:
            role = 'BLOGGER'

        table.add_row([person.get('username'), role, person.get('email')])

    print(table)


def remove_user_by_username(username: str) -> Union[bool, int, None]:
    """
    To remove a user by username
    """
    try:
        user_status = Database.get_item(Sql.GET_USER_BY_USERNAME.value, (username,))

        if not user_status:
            return False

        user_to_remove = User(*user_status[1:])
        user_to_remove.user_role = int(user_to_remove.user_role)

        if user_to_remove.user_role == Role.ADMIN.value:
            print(prompts.ADMIN_CANT_BE_REMOVED)
            return Flag.INVALID_OPERATION.value

        user_to_remove.remove_user_by_username()

        GeneralLogger.info(prompts.USER_WITH_USERNAME_REMOVED.format(username), filepaths.USER_LOG_FILE)

        return True

    except Exception as exc:
        GeneralLogger.error(exc, filepaths.USER_LOG_FILE)
        return False


def view_blogs() -> None:
    """
    To view all the blogs posted so far
    """
    blogs = Database.get_items(Sql.GET_ALL_BLOGS.value)

    if blogs is None:
        print(prompts.BLOGS_NOT_FOUND)
        return

    blogs = [Blog(blog[1:]) for blog in blogs]

    for blog in blogs:
        print(blog.details())


def view_blogs_by_user(username: str) -> None:
    """
    To view blogs by a particular user using his username
    """
    blogs = Database.get_items(Sql.GET_BLOGS_BY_USERNAME.value, (username,))

    if len(blogs) < 1:
        blogs = None

    if blogs is None:
        print(prompts.NO_BLOG_BY_USER.format(username))
        return

    blogs = [Blog(blog[1:]) for blog in blogs]
    for blog in blogs:
        print(blog.details())


def view_blogs_by_tag_name(tag_name: str) -> None:
    """
    To view blogs filtered by the tag name
    """
    blogs = Database.get_items(Sql.GET_BLOGS_BY_TAG_NAME.value, (tag_name,))

    if len(blogs) < 1:
        blogs = None

    if blogs is None:
        print(prompts.NO_BLOG_OF_TAG_NAME.format(tag_name))
        return

    blogs = [Blog(blog[1:]) for blog in blogs]

    for blog in blogs:
        print(blog.details())


def view_one_blog() -> bool:
    """
    View a particular blog by its name
    """
    title = take_input.get_title()
    blog_details = Database.get_item(Sql.GET_BLOG_RECORD_BY_TITLE.value, (title,))

    if blog_details is None:
        print(prompts.BLOG_NOT_FOUND_NAME.format(title))
        return Flag.DOES_NOT_EXIST.value

    current_blog = Blog(blog_details[1:])
    current_blog.set_blog_id(blog_details[0])

    print(current_blog.details())

    blog_comments = current_blog.get_comments()
    if blog_comments:
        print(prompts.COMMENTS)

        for record in blog_comments:
            print(record.details())

    return True


def create_blog(active_user: User) -> None:
    """
    This function allows the user to create a new blog
    """
    title, content, tag = take_input.get_blog_post_details()
    blog_details = Database.get_item(Sql.GET_BLOG_RECORD_BY_TITLE.value, (title,))

    if blog_details:
        print(prompts.CHOOSE_ANOTHER_TITLE)
        return

    current_date = datetime.today()
    blog_post_d = (title, content, active_user.username, 0, tag, current_date)

    new_blog = Blog(blog_post_d)
    blog_added = new_blog.add_content()
    if blog_added:
        print(prompts.BLOG_ADDED.format(title))


def edit_blog(active_user: User) -> None:
    """
    This function allows the user to edit his blog if it exists
    """
    title = take_input.get_title()
    blog_details = Database.get_item(Sql.GET_BLOG_RECORD.value, (title, active_user.username))

    if blog_details is None:
        print(prompts.BLOG_NOT_FOUND_BLOG_USER.format(title, active_user.username))
        return Flag.DOES_NOT_EXIST.value

    current_blog = Blog(blog_details[1:])
    current_blog.set_blog_id(blog_details[0])

    new_content = take_input.get_new_content()
    edited = current_blog.edit_content(new_content)

    if edited:
        print(prompts.BLOG_EDITED.format(title))

    else:
        print(prompts.COULD_NOT_EDIT_BLOG.format(title))


def remove_blog(active_user: User) -> None:
    """
    This function allows the user to remove his blog
    """
    title = take_input.get_title()
    blog_details = Database.get_item(Sql.GET_BLOG_RECORD.value, (title, active_user.username))

    if blog_details is None:
        print(prompts.BLOG_NOT_FOUND_BLOG_USER.format(title, active_user.username))
        return Flag.DOES_NOT_EXIST.value

    # create blog object
    current_blog = Blog(blog_details[1:])
    current_blog.set_blog_id(blog_details[0])

    blog_removed = current_blog.remove_content()

    if blog_removed:
        print(prompts.BLOG_REMOVED.format(title))
        GeneralLogger.info(prompts.BLOG_REMOVED.format(title), filepaths.BLOG_LOG_FILE)

    else:
        print(prompts.COULD_NOT_REMOVE_BLOG)


@admin
def admin_remove_blog(active_user: User) -> None:
    """
    This function allows the admin to remove any blog
    """

    title = take_input.get_title()
    blog_details = Database.get_item(Sql.GET_BLOG_RECORD_BY_TITLE.value, (title,))

    if blog_details is None:
        print(prompts.BLOG_NOT_FOUND_NAME.format(title, ))
        return Flag.DOES_NOT_EXIST.value

    current_blog = Blog(blog_details[1:])
    current_blog.set_blog_id(blog_details[0])

    blog_removed = current_blog.remove_content_by_title()

    if blog_removed:
        print(prompts.BLOG_REMOVED.format(title))
        GeneralLogger.info(prompts.BLOG_REMOVED.format(title), filepaths.BLOG_LOG_FILE)

    else:
        print(prompts.COULD_NOT_REMOVE_BLOG)


def upvote_blog(active_user: User) -> None:
    """
    This function allows the user to upvote any blog that exists.
    """
    title = take_input.get_title()
    blog_details = Database.get_item(Sql.GET_BLOG_RECORD_BY_TITLE.value, (title,))

    if blog_details is None:
        print(prompts.BLOG_NOT_FOUND_NAME.format(title))
        return Flag.DOES_NOT_EXIST.value

    current_blog = Blog(blog_details[1:])
    current_blog.set_blog_id(blog_details[0])

    upvoted = current_blog.upvote(active_user.user_id)

    if upvoted:
        print(prompts.UPVOTED_BLOG.format(title))

    else:
        print(prompts.COULD_NOT_UPVOTE_BLOG.format(title))


def comment_on_blog(active_user: User) -> None:
    """
    This function allows the user to comment on a blog that exists.
    """
    title = take_input.get_title()
    blog_details = Database.get_item(Sql.GET_BLOG_RECORD_BY_TITLE.value, (title,))

    if blog_details is None:
        print(prompts.BLOG_NOT_FOUND_NAME.format(title))
        return Flag.DOES_NOT_EXIST.value

    current_blog = Blog(blog_details[1:])
    current_blog.set_blog_id(blog_details[0])

    content = take_input.get_comment()
    current_time = datetime.today()

    comment_info = (current_blog.blog_id, content, active_user.username, 0, current_time)

    new_comment = Comment(comment_info)
    status = new_comment.add_content()

    if status:
        print(prompts.COMMENT_ADDED)
        GeneralLogger.info(prompts.USER_COMMENTED.format(active_user.username, title), filepaths.BLOG_LOG_FILE)

    else:
        print(prompts.COMMENT_NOT_ADDED)
