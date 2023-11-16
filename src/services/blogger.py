from datetime import datetime

from src.common import prompts
from src.helpers import take_input, validation
from src.helpers.admin_only import admin
from src.controllers.blog import Blog
from src.controllers.comment import Comment
from src.common.sql_query import Sql
from src.controllers.authentication import Authentication
from src.controllers.user import User
from src.common.flags import Flag
from src.common.roles import Role
from src.models import database
from src.loggers.general_logger import GeneralLogger
from src.common import filepaths


def blogger_menu(active_user):
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
        view_one_blog()
        blogger_menu(active_user)

    elif choice == '4':
        create_blog(active_user)
        blogger_menu(active_user)

    elif choice == '5':
        edit_blog(active_user)
        blogger_menu(active_user)

    elif choice == '6':
        remove_blog(active_user)
        blogger_menu(active_user)

    elif choice == '7':
        upvote_blog(active_user)
        blogger_menu(active_user)

    elif choice == '8':
        comment_on_blog(active_user)
        blogger_menu(active_user)

    elif choice == '9':
        change_password(active_user)
        blogger_menu(active_user)

    elif choice == '10':
        pass

    else:
        print(prompts.ENTER_VALID_CHOICE)
        blogger_menu(active_user)


def admin_menu(active_user):
    menu_prompt = prompts.ADMIN_SPECIFIC

    choice = input(menu_prompt)

    if choice == '1':
        view_blogs()
        admin_menu(active_user)

    elif choice == '2':
        username = take_input.get_user_for_blog()

        view_blogs_by_user(username)
        admin_menu(active_user)

    elif choice == '3':
        view_one_blog()
        admin_menu(active_user)

    elif choice == '4':
        create_blog(active_user)
        admin_menu(active_user)

    elif choice == '5':
        edit_blog(active_user)
        admin_menu(active_user)

    elif choice == '6':
        remove_blog(active_user)
        admin_menu(active_user)

    elif choice == '7':
        upvote_blog(active_user)
        admin_menu(active_user)

    elif choice == '8':
        comment_on_blog(active_user)
        admin_menu(active_user)

    elif choice == '9':
        users = get_users(active_user)
        users = [dict(user.get_details()) for user in users]

        display_users(users)
        admin_menu(active_user)

    elif choice == '10':
        user_to_remove = input(prompts.ENTER_USERNAME_TO_REMOVE)
        status = remove_user_by_username(user_to_remove)

        if status:
            print(prompts.USER_REMOVED)

        admin_menu(active_user)

    elif choice == '11':
        change_password(active_user)
        admin_menu(active_user)

    elif choice == '12':
        pass

    else:
        print(prompts.ENTER_VALID_CHOICE)
        admin_menu(active_user)


@admin
def get_users(active_user):
    try:
        user_list = database.get_items(Sql.GET_ALL_USERS.value)
        users = [User(*record[1:]) for record in user_list]

        return users
    except Exception as exc:
        print(exc)


def change_password(active_user):
    new_passw = take_input.get_new_password()

    if validation.validate_password(new_passw):
        hashed_passw = Authentication().hash_password(new_passw)

        if active_user.change_password(hashed_passw):
            print(prompts.SUCCESSFUL_PASSWORD_CHANGE)
            GeneralLogger.info(prompts.USER_CHANGED_PASSWORD.format(active_user.username), filepaths.USER_LOG_FILE)

    else:
        print(prompts.ENTER_STRONG_PASSWORD)
        change_password(active_user)


def display_users(user_list):
    print(prompts.USERS_HEADER)

    print(prompts.DISPLAY_USER_HEADER)

    for person in user_list:
        role = int(person['role'])

        if role == Role.ADMIN.value:
            role = 'ADMIN'

        elif role == Role.BLOGGER.value:
            role = 'BLOGGER'

        print(prompts.USER_INFO.format(person['username'], role, person['email']))


def remove_user_by_username(username):
    try:
        database.remove_item(Sql.REMOVE_USER_BY_USERNAME.value, (username,))
        GeneralLogger.info(prompts.USER_WITH_USERNAME_REMOVED.format(username), filepaths.USER_LOG_FILE)

        return True

    except Exception as exc:
        GeneralLogger.error(exc, filepaths.USER_LOG_FILE)
        return False


def view_blogs():
    blogs = database.get_items(Sql.GET_ALL_BLOGS.value)

    if blogs is None:
        print(prompts.BLOGS_NOT_FOUND)
        return

    blogs = [Blog(blog[1:]) for blog in blogs]

    for blog in blogs:
        print(blog.details())


def view_blogs_by_user(username):
    blogs = database.get_items(Sql.GET_BLOGS_BY_USERNAME.value, (username,))

    if len(blogs) < 1:
        blogs = None

    if blogs is None:
        print(prompts.NO_BLOG_BY_USER.format(username))
        return

    blogs = [Blog(blog[1:]) for blog in blogs]

    for blog in blogs:
        print(blog.details())


def view_one_blog():
    title = input(prompts.ENTER_BLOG_TITLE)
    blog_details = database.get_item(Sql.GET_BLOG_RECORD_BY_TITLE.value, (title,))

    if blog_details is None:
        print(prompts.BLOG_NOT_FOUND_NAME.format(title))
        return Flag.DOES_NOT_EXIST.value

    current_blog = Blog(blog_details[1:])
    current_blog.set_blog_id(blog_details[0])

    print(current_blog.details())

    blog_comments = current_blog.get_comments()

    print(prompts.COMMENTS)

    for record in blog_comments:
        print(record.details())

    return True


def create_blog(active_user):
    title, content, tag = take_input.get_blog_post_details()
    blog_details = database.get_item(Sql.GET_BLOG_RECORD_BY_TITLE.value, (title,))

    if blog_details:
        print(prompts.CHOOSE_ANOTHER_TITLE)
        return

    current_date = datetime.today()
    blog_post_d = (title, content, active_user.username, 0, tag, current_date)

    new_blog = Blog(blog_post_d)
    new_blog.add_content()

    print(prompts.BLOG_ADDED.format(title))


def edit_blog(active_user):
    title = take_input.get_title()
    blog_details = database.get_item(Sql.GET_BLOG_RECORD.value, (title, active_user.username))

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


def remove_blog(active_user):
    title = take_input.get_title()
    blog_details = database.get_item(Sql.GET_BLOG_RECORD.value, (title, active_user.username))

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


def upvote_blog(active_user):
    title = take_input.get_title()
    blog_details = database.get_item(Sql.GET_BLOG_RECORD_BY_TITLE.value, (title,))

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


def comment_on_blog(active_user):
    title = take_input.get_title()
    blog_details = database.get_item(Sql.GET_BLOG_RECORD_BY_TITLE.value, (title,))

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
