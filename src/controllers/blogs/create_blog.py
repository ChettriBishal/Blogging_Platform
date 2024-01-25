from controllers.blog import Blog
from datetime import datetime
from utils.users.get_current_user import GetCurrentUser
from handlers.blogs.add_blog_handler import AddBlogHandler


class CreateBlog:
    """
        This function allows the user to create a new blog
    """

    @staticmethod
    def create_new_blog(title, content, tag):
        current_date = datetime.today()
        current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

        blog_post_d = (title, content, GetCurrentUser.get_user_name(), 0, tag, current_date)

        new_blog = Blog(blog_post_d)
        blog_added = AddBlogHandler.add_new_blog(new_blog)
        if blog_added:
            return True

        return False
