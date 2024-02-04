from models.database import Database
from config.sql_query_mysql import Sql
from loggers.general_logger import GeneralLogger
from config import filepaths
from utils.exceptions import DbException
from config.message import Message


class UpdateBlogHandler:
    @staticmethod
    def update_blog_title(blog_id, new_title):
        """Update the title of the blog"""
        try:
            Database.query_with_params(Sql.EDIT_BLOG_TITLE.value, (new_title, blog_id,))
            return True
        except DbException as exc:
            GeneralLogger.error(exc.message, filepaths.BLOG_LOG_FILE)
            raise DbException(code=exc.code, message=Message.COULD_NOT_UPDATE_TITLE)

    @staticmethod
    def update_blog_content(blog_id, new_content):
        """Update the actual content of a specific blog"""
        try:
            Database.query_with_params(Sql.EDIT_BLOG_CONTENT.value, (new_content, blog_id,))
            return True
        except DbException as exc:
            GeneralLogger.error(exc.message, filepaths.BLOG_LOG_FILE)
            raise DbException(code=exc.code, message=Message.COULD_NOT_UPDATE_CONTENT_BLOG)

    @staticmethod
    def update_blog_tag(blog_id, new_tag):
        """Update the blog tag for a given blog"""
        try:
            Database.query_with_params(Sql.EDIT_BLOG_TAG.value, (new_tag, blog_id,))
            return True
        except DbException as exc:
            GeneralLogger.error(exc, filepaths.BLOG_LOG_FILE)
            raise DbException(code=exc.code, message=Message.FAILURE_IN_UPDATE)
