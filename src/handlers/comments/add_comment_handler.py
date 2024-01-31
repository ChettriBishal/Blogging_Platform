from models.database import Database
from config.sql_query_mysql import Sql
from loggers.general_logger import GeneralLogger
from config import filepaths
from typing import Union


class AddCommentHandler:
    @staticmethod
    def add_new_comment(comment_details) -> Union[int, bool, None]:
        try:
            comment_id = Database.insert_item(Sql.INSERT_COMMENT.value, comment_details)
            if comment_id:
                return comment_id
            return False

        except Exception as exc:
            # create a custom exception to handle this
            GeneralLogger.error(exc, filepaths.COMMENT_LOG_FILE)
