from typing import Union
from config.sql_query_mysql import Sql
from models.database import Database
from loggers.general_logger import GeneralLogger
from config import filepaths
from utils.exceptions import DbException
from config.message import Message


class AddBlogHandler:
    @staticmethod
    def add_new_blog(blog_details) -> Union[int, bool]:
        """Makes database call for inserting a new blogs"""
        try:
            blog_id = Database.insert_item(Sql.INSERT_BLOG.value, blog_details)
            if blog_id:
                return blog_id
            return False

        except DbException as exc:
            GeneralLogger.error(exc.message, filepaths.BLOG_LOG_FILE)
            raise DbException(code=exc.code, message=Message.COULD_NOT_ADD_BLOG)
