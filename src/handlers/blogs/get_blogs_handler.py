from models.database import Database
from config.sql_query_mysql import Sql


class GetBlogsHandler:
    @staticmethod
    def blog_collection():
        blogs = Database.get_items(Sql.GET_ALL_BLOGS.value)
        return blogs

    @staticmethod
    def blog_by_id(blog_id):
        blog = Database.get_item(Sql.GET_BLOG_BY_BLOG_ID.value, (blog_id,))
        return blog

    @staticmethod
    def blogs_by_username(username):
        blogs = Database.get_items(Sql.GET_BLOGS_BY_USERNAME.value, username)
        return blogs

    @staticmethod
    def blogs_by_userid(userid):
        blogs = Database.get_items(Sql.GET_BLOGS_BY_USERID.value, (userid,))
        return blogs
