from models.database import Database
from config.sql_query_mysql import Sql
from utils.exceptions import DbException


class BlogInfoHandler:
    @staticmethod
    def get_creator_id_from_blog_id(blog_id):
        """Get the creator ID using the blog ID -> Blog writer"""
        try:
            creator_id = Database.get_item(Sql.GET_CREATOR_ID_FROM_BLOG_ID.value, (blog_id,))[0]
            return creator_id
        except DbException:
            raise DbException
