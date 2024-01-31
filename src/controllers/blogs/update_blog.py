from handlers.blogs.update_blog_handler import UpdateBlogHandler
from utils.users.get_current_user import GetCurrentUser
from handlers.user.user_info_handler import UserInfoHandler
from handlers.blogs.blog_info_handler import BlogInfoHandler


# you can update the title, tag or the content nothing else
class UpdateBlog:
    def __init__(self, **kwargs):
        self.blog_id = kwargs.get('blog_id')
        self.title = kwargs.get('title')
        self.content = kwargs.get('content')
        self.tag = kwargs.get('tag')

    def authenticate_user(self):
        current_userid = GetCurrentUser.get_user_id()
        creator_id = BlogInfoHandler.get_creator_id_from_blog_id(self.blog_id)
        if current_userid != creator_id:
            return False
        return True

    def update_title(self):
        """Update the title of the blog"""
        if self.title:
            update_status = UpdateBlogHandler.update_blog_title(self.blog_id, self.title)
            return update_status

    def update_content(self):
        """Update the actual blog content"""
        if self.content:
            update_status = UpdateBlogHandler.update_blog_content(self.blog_id, self.content)
            return update_status

    def update_tag(self):
        """Update the tag of the blog"""
        if self.tag:
            update_status = UpdateBlogHandler.update_blog_tag(self.blog_id, self.tag)
            return update_status

