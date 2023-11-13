from datetime import datetime

from src.common import prompts
from src.helpers import take_input
from src.controllers.blog import Blog
from src.common.sql_query import Sql
from src.controllers.authentication import Authentication
from src.controllers.user import User
from src.common.flags import Flag
from src.common.roles import Role

from src.models import database


def blogger_menu(active_user):
    choice = input(prompts.BLOGGER_MENU)
    if choice == '1':
        view_blogs(active_user)
        blogger_menu(active_user)
    elif choice == '2':
        create_blog(active_user)
        blogger_menu(active_user)
    elif choice == '3':
        edit_blog(active_user)
        blogger_menu(active_user)
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    else:
        print("Please enter a valid choice!")


def view_blogs(active_user):
    pass


def create_blog(active_user):
    title, content, tag = take_input.get_blog_post_details()
    current_date = datetime.today()
    # blog_post_d = ('YUI', 'just testing', 'snow123', 0, 'test', '2023-11-11 18:16:08.792008')
    blog_post_d = (title, content, active_user.username, 0, tag, current_date)
    new_blog = Blog(blog_post_d)
    new_blog.add_content()
    # new_blog.show_details()


def edit_blog(active_user):
    # which blog do you want to edit?
    title = take_input.get_title()
    blog_details = database.get_item(Sql.GET_BLOG_RECORD.value, (title, active_user.username))
    if blog_details is None:
        return Flag.DOES_NOT_EXIST.value

    # create blog object
    current_blog = Blog(blog_details[1:])
    current_blog.set_blog_id(blog_details[0])

    if current_blog.creator != active_user.username:
        raise PermissionError("Only the creator can edit blogs")

    new_content = take_input.get_new_content()
    edited = current_blog.edit_content(new_content)
    if edited:
        print("Blog edited successfully!")
    else:
        print("Could not edit the blog")


def remove_blog(active_user):
    # which blog do you want to remove
    title = take_input.get_title()
    blog_details = database.get_item(Sql.GET_BLOG_RECORD.value, (title, active_user.username))
    if blog_details is None:
        return Flag.DOES_NOT_EXIST.value

    # create blog object
    current_blog = Blog(blog_details[1:])
    current_blog.set_blog_id(blog_details[0])

    if current_blog.creator != active_user.username:
        raise PermissionError("Only the creator can delete blogs")

    blog_removed = current_blog.remove_content()

    if blog_removed:
        print("Blog removed successfully!")
    else:
        print("Could not remove the blog")


if __name__ == "__main__":
    user_info = ('snow123', '4ac22cda6741c8c6259b69ca423f455f9149c6fa8c8fbec5060ef0a749af81f3', 2, 'snow', '2023-11-09')

    current_user = User(*user_info)
    # create_blog(current_user)
    # edit_blog(current_user)
    remove_blog(current_user)
    print(current_user.get_details())
