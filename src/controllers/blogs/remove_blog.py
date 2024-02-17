from utils.users.get_current_user import GetCurrentUser
from handlers.blogs.blog_info_handler import BlogInfoHandler
from handlers.blogs.remove_blog_handler import RemoveBlogHandler
from utils.exceptions import DbException
from config.message import Message


class RemoveBlog:
    def __init__(self, **kwargs):
        self.blog_id = kwargs.get('blog_id')

    def authenticate_user(self):
        """Check if the user in session was the actual creator"""
        current_user_role = GetCurrentUser.get_user_role()
        if int(current_user_role) == 1:  # if admin
            return True

        current_userid = GetCurrentUser.get_user_id()
        creator_id = BlogInfoHandler.get_creator_id_from_blog_id(self.blog_id)
        if current_userid != creator_id:
            return False
        return True

    def remove_blog_by_id(self):
        """Remove blog by id"""
        try:
            if not self.authenticate_user():
                return {"message": Message.OPERATION_NOT_ALLOWED}, 403
            blog_removed = RemoveBlogHandler.remove_blog(self.blog_id)
            if blog_removed:
                return {"message": Message.SUCCESSFUL_REMOVAL}, 200
            return {"message": Message.FAILURE_IN_REMOVAL}, 500
        except DbException as exc:
            return exc.dump()
