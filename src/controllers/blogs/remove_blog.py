from utils.users.get_current_user import GetCurrentUser
from handlers.blogs.blog_info_handler import BlogInfoHandler
from handlers.blogs.remove_blog_handler import RemoveBlogHandler


class RemoveBlog:
    def __init__(self, **kwargs):
        self.blog_id = kwargs.get('blog_id')

    def authenticate_user(self):
        """Check if the user in session was the actual creator"""
        current_userid = GetCurrentUser.get_user_id()
        creator_id = BlogInfoHandler.get_creator_id_from_blog_id(self.blog_id)
        if current_userid != creator_id:
            return False
        return True

    def remove_blog_by_id(self):
        """Remove blog by id"""
        blog_removed = RemoveBlogHandler.remove_blog(self.blog_id)
        return blog_removed


