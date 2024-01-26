from controllers.blog import Blog
from datetime import datetime
from utils.users.get_current_user import GetCurrentUser
from handlers.blogs.add_blog_handler import AddBlogHandler
from config.flags import Flag
from typing import Tuple


class CreateBlog:
    """
        This function allows the user to create a new blog
    """

    def __init__(self, blog_info_received):
        self.blog_info = blog_info_received
        (
            self.title,
            self.content,
            self.tag
        ) = blog_info_received
        self.creation_date: str

    def create_blog_details_obj(self, username) -> Tuple:
        current_date = datetime.today()
        current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
        resultant_blog_info = (self.title, self.content, username, 0, self.tag, current_date)
        return resultant_blog_info

    def create_new_blog(self) -> bool:

        # get the current username from the jwt token
        username = GetCurrentUser.get_user_name()
        blog_post_d = self.create_blog_details_obj(username)

        print("In create_blog controller")
        # blog_added = new_blog.add_content()
        blog_added = AddBlogHandler.add_new_blog(blog_post_d)
        if blog_added:
            return True

        return False
