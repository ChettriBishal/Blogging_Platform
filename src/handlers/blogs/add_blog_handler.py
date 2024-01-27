from typing import Union, Tuple, List
from controllers.post import Post
from config.sql_query_mysql import Sql
from models.database import Database
from controllers.comment import Comment
from loggers.general_logger import GeneralLogger
from config import filepaths
from config import prompts


class AddBlogHandler:
    @staticmethod
    def add_new_blog(blog_details) -> Union[int, bool]:
        """Makes database call for inserting a new blog"""
        try:
            blog_id = Database.insert_item(Sql.INSERT_BLOG.value, blog_details)
            if blog_id:
                return blog_id
            return False

        except Exception as exc:
            # create a custom exception to handle this
            GeneralLogger.error(exc, filepaths.BLOG_LOG_FILE)
