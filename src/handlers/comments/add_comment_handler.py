from models.database import Database
from config.sql_query_mysql import Sql
from loggers.general_logger import GeneralLogger
from config import filepaths
from typing import Union
from utils.exceptions import DbException
from config.message import Message


class AddCommentHandler:
    @staticmethod
    def add_new_comment(comment_details) -> Union[int, bool, None]:
        """To add a new comment into the DB"""
        try:
            comment_id = Database.insert_item(Sql.INSERT_COMMENT.value, comment_details)
            if comment_id:
                return comment_id
            return False

        except DbException as exc:
            GeneralLogger.error(exc, filepaths.COMMENT_LOG_FILE)
            raise DbException(exc.code, Message.COULD_NOT_COMMENT)
