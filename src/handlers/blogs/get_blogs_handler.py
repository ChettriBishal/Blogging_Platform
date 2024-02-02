from models.database import Database
from config.sql_query_mysql import Sql


class GetBlogsHandler:
    @staticmethod
    def blog_collection():
        """Get all blogs"""
        blogs = Database.get_items(Sql.GET_ALL_BLOGS.value)
        return blogs

    @staticmethod
    def blog_by_id(blog_id):
        """Get a specific blog by ID"""
        blog = Database.get_item(Sql.GET_BLOG_BY_BLOG_ID.value, (blog_id,))
        return blog

    @staticmethod
    def blogs_by_username(username):
        """Get all blogs written by a particular user"""
        blogs = Database.get_items(Sql.GET_BLOGS_BY_USERNAME.value, username)
        return blogs

    @staticmethod
    def blogs_by_userid(userid):
        """Get all blogs written by a specific user's ID """
        blogs = Database.get_items(Sql.GET_BLOGS_BY_USERID.value, (userid,))
        return blogs
