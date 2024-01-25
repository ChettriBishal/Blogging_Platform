from controllers.blog import Blog
from config import prompts
from handlers.blogs.get_blogs_handler import GetBlogsHandler


class GetBlogs:
    @staticmethod
    def get_all_blogs():
        """
        To get all the blogs posted so far
        """
        blogs = GetBlogsHandler.blog_collection()
        return blogs

    @staticmethod
    def get_single_blog():
        """Get a single blog by id"""

    @staticmethod
    def get_blogs_by_username(username):
        """Get blogs by a specific user"""
        """
            To view blogs by a particular user using his username
            """
        blogs = GetBlogsHandler.blogs_by_username(username)

        if len(blogs) < 1:
            blogs = None

        if blogs is None:
            print(prompts.NO_BLOG_BY_USER.format(username))
            return

        blogs = [Blog(blog[1:]) for blog in blogs]
        for blog in blogs:
            print(blog.details())

