from models.database import Database
from config.sql_query_mysql import Sql
from config.filepaths import COMMENT_LOG_FILE
from loggers.general_logger import GeneralLogger
from config import prompts, filepaths


class RemoveCommentHandler:
    @staticmethod
    def remove_comment_by_id(comment_id):
        """
        Method to remove content of the comments
        """
        try:
            Database.remove_item(Sql.REMOVE_COMMENT_BY_ID.value, (comment_id,))
            return True
        except Exception as exc:
            GeneralLogger.error(exc, COMMENT_LOG_FILE)
            return False

    @staticmethod
    def remove_comment_by_blog_id(blog_id):
        """Remove all comments by blog id"""
        all_comments = Database.get_items(Sql.GET_COMMENTS_BY_BLOG_ID.value, (blog_id,))
        if not all_comments:
            return None

        for comment_id in all_comments:
            comment_to_remove = comment_id[0]
            Database.remove_item(Sql.REMOVE_COMMENT_BY_ID.value, (comment_to_remove,))

            GeneralLogger.info(prompts.REMOVED_COMMENT_WITH_ID.format(comment_id[0]), filepaths.COMMENT_LOG_FILE)

        return True
