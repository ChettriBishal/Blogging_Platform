from datetime import datetime

from src.common import prompts
from src.helpers import take_input
from src.helpers.admin_only import admin
from src.controllers.blog import Blog
from src.controllers.comment import Comment
from src.common.sql_query import Sql
from src.controllers.authentication import Authentication
from src.controllers.user import User
from src.common.flags import Flag
from src.common.roles import Role

from src.models import database


def blogger_menu(active_user):
    menu_prompt = prompts.BLOGGER_MENU

    choice = input(menu_prompt)
    if choice == '1':
        view_blogs()
        blogger_menu(active_user)
    elif choice == '2':
        view_one_blog()
        blogger_menu(active_user)
    elif choice == '3':
        create_blog(active_user)
        blogger_menu(active_user)
    elif choice == '4':
        edit_blog(active_user)
        blogger_menu(active_user)
    elif choice == '5':
        remove_blog(active_user)
        blogger_menu(active_user)
    elif choice == '6':
        upvote_blog(active_user)
        blogger_menu(active_user)
    elif choice == '7':
        comment_on_blog(active_user)
        blogger_menu(active_user)
    elif choice == '8':
        pass
    else:
        print("Please enter a valid choice!")
        blogger_menu(active_user)


def admin_menu(active_user):
    menu_prompt = prompts.ADMIN_SPECIFIC

    choice = input(menu_prompt)
    if choice == '1':
        view_blogs()
        admin_menu(active_user)
    elif choice == '2':
        view_one_blog()
        admin_menu(active_user)
    elif choice == '3':
        create_blog(active_user)
        admin_menu(active_user)
    elif choice == '4':
        edit_blog(active_user)
        admin_menu(active_user)
    elif choice == '5':
        remove_blog(active_user)
        admin_menu(active_user)
    elif choice == '6':
        upvote_blog(active_user)
        admin_menu(active_user)
    elif choice == '7':
        comment_on_blog(active_user)
        admin_menu(active_user)
    elif choice == '8':
        users = get_users(active_user)
        users = [dict(user.get_details()) for user in users]
        # for u1 in users:
        #     print(u1.get_details())
        display_users(users)
        admin_menu(active_user)
    elif choice == '9':
        user_to_remove = input(prompts.ENTER_USERNAME_TO_REMOVE)
        status = remove_user_by_username(user_to_remove)
        if status:
            print("User removed successfully!")
        admin_menu(active_user)
    elif choice == '10':
        pass
    else:
        print("Please enter a valid choice!")
        admin_menu(active_user)


@admin
def get_users(active_user):
    try:
        user_list = database.get_items(Sql.GET_ALL_USERS.value)
        users = [User(*record[1:]) for record in user_list]
        return users
    except Exception as exc:
        print(exc)


def display_users(user_list):
    print("--------------Users--------------")
    print(f"\nUsername\t\tRole\t\tEmail")
    for person in user_list:
        role = int(person['role'])
        if role == Role.ADMIN.value:
            role = 'ADMIN'
        elif role == Role.BLOGGER.value:
            role = 'BLOGGER'
        # print(f"username: {person['username']} | role: {role} | Email: {person['email']}")
        print(f"{person['username']}\t|\t{role}\t|\t{person['email']}")


def remove_user_by_username(username):
    try:
        database.remove_item(Sql.REMOVE_USER_BY_USERNAME.value, (username,))
        return True
    except Exception as exc:
        print(exc)
        return False


def view_blogs():
    # this user should be able to view all blogs
    blogs = database.get_items(Sql.GET_ALL_BLOGS.value)
    blogs = [Blog(blog[1:]) for blog in blogs]

    for blog in blogs:
        print(blog.details())


def view_one_blog():
    title = input(prompts.ENTER_BLOG_TITLE)
    blog_details = database.get_item(Sql.GET_BLOG_RECORD_BY_TITLE.value, (title,))
    if blog_details is None:
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


def upvote_blog(active_user):
    title = take_input.get_title()
    blog_details = database.get_item(Sql.GET_BLOG_RECORD_BY_TITLE.value, (title,))
    if blog_details is None:
        return Flag.DOES_NOT_EXIST.value

    # create blog object
    current_blog = Blog(blog_details[1:])
    current_blog.set_blog_id(blog_details[0])

    # if current_blog.creator != active_user.username:
    #     raise PermissionError("Only the creator can delete blogs")
    upvoted = current_blog.upvote(active_user.user_id)
    if upvoted:
        print(f"{title} is upvoted successfully!")


def comment_on_blog(active_user):
    title = take_input.get_title()
    blog_details = database.get_item(Sql.GET_BLOG_RECORD_BY_TITLE.value, (title,))
    if blog_details is None:
        return Flag.DOES_NOT_EXIST.value

    current_blog = Blog(blog_details[1:])
    current_blog.set_blog_id(blog_details[0])

    content = take_input.get_comment()
    current_time = datetime.today()

    comment_info = (current_blog.blog_id, content, active_user.username, 0, current_time)

    new_comment = Comment(comment_info)
    status = new_comment.add_content()
    if status:
        print("Comment added successfully!")


if __name__ == "__main__":
    user_info = ('snow123', '4ac22cda6741c8c6259b69ca423f455f9149c6fa8c8fbec5060ef0a749af81f3', 2, 'snow', '2023-11-09')

    current_user = User(*user_info)
    # create_blog(current_user)
    # edit_blog(current_user)
    # remove_blog(current_user)
    print(current_user.get_details())
    # view_blogs(current_user)
    # blogger_menu(current_user)
    view_one_blog()
