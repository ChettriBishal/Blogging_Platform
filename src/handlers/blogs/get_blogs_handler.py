from models.database import Database
from config.sql_query_mysql import Sql


class GetBlogsHandler:
    @staticmethod
    def blog_collection():
        blogs = Database.get_items(Sql.GET_ALL_BLOGS.value)
        return blogs

    def blog_by_id(self):
        pass

    @staticmethod
    def blogs_by_username(username):
        blogs = Database.get_items(Sql.GET_BLOGS_BY_USERNAME.value, (username,))
        return blogs