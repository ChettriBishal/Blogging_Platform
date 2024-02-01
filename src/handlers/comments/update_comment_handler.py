from models.database import Database
from config.sql_query_mysql import Sql
from loggers.general_logger import GeneralLogger
from config import filepaths


class UpdateCommentHandler:
    @staticmethod
    def update_comment(comment_id, new_content):
        """This function allows us to edit the comment"""
        try:
            Database.query_with_params(Sql.EDIT_COMMENT.value, (new_content, comment_id,))
            return True
        except Exception as exc:
            GeneralLogger.error(exc, filepaths.BLOG_LOG_FILE)
            return False
