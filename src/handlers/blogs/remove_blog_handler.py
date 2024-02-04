from models.database import Database
from config.sql_query_mysql import Sql
from loggers.general_logger import GeneralLogger
from handlers.comments.remove_comment_handler import RemoveCommentHandler
from config import filepaths
from config.message import Message
from utils.exceptions import DbException


class RemoveBlogHandler:
    @staticmethod
    def remove_blog(blog_id):
        """
        This function allows the user to remove his blogs
        """
        try:
            # firstly remove all the comments of the blog
            RemoveCommentHandler.remove_comment_by_blog_id(blog_id)
            # then remove the blog
            Database.remove_item(Sql.REMOVE_BLOG_BY_ID.value, (blog_id,))
            return True

        except DbException as exc:
            GeneralLogger.error(exc, filepaths.BLOG_LOG_FILE)
            raise DbException(exc.code, Message.FAILURE_IN_REMOVAL)


