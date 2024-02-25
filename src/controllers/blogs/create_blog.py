from datetime import datetime
from handlers.blogs.add_blog_handler import AddBlogHandler
from typing import Tuple, Any
from utils.exceptions import DbException
from config.message import Message


class CreateBlog:
    """
        This allows the user to create a new blogs
    """

    def __init__(self, blog_info_received):
        self.creation_date = None
        self.user_id = None  # added externally after object creation
        self.blog_info = blog_info_received
        (
            self.title,
            self.content,
            self.tag
        ) = blog_info_received

    def create_blog_details_obj(self) -> Tuple:
        """This creates a details object as per the database schema"""
        current_date = datetime.now()
        self.creation_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
        resultant_blog_info = (self.title, self.content, self.user_id, 0, self.tag, current_date)
        return resultant_blog_info

    def create_new_blog(self) -> tuple[dict[str, Any], int] | bool | Any:
        """To create a new blog"""
        try:
            blog_post_d = self.create_blog_details_obj()
            blog_added = AddBlogHandler.add_new_blog(blog_post_d)
            if blog_added:
                return {"blogId": blog_added, "message": Message.SUCCESSFUL_POST}, 201
            return {"message": Message.FAILURE_IN_POST}, 500
        except DbException as exc:
            return exc.dump()
