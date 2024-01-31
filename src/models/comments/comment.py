"""This module contains the various operations on a comments"""

from typing import Union, Tuple
from models.post import Post
from config.sql_query_mysql import Sql
from models.database import Database
from config import prompts
from loggers.general_logger import GeneralLogger
from config.filepaths import COMMENT_LOG_FILE


class Comment(Post):
    """
    Class containing various methods associated with a comments object
    """
    def __init__(self, comment_info: Tuple) -> None:
        (
            # comment_id will be auto incremented
            self.blog_id,
            self.content,
            self.creator,
            self.upvotes,
            self.creation_date,
        ) = comment_info
        self.comment_id = None
        self.comment_info = comment_info

    def add_content(self) -> Union[bool, None]:
        """
        Method to add new comments content
        """
        try:
            self.comment_id = Database.insert_item(Sql.INSERT_COMMENT.value, self.comment_info)
            if self.comment_id:
                return True

        except Exception as exc:
            GeneralLogger.error(exc, COMMENT_LOG_FILE)

    def edit_content(self, new_content: str) -> Union[bool, None]:
        """
        Method to edit content of the comments
        """
        try:
            comment_id = Database.get_item(Sql.GET_COMMENT_ID.value, (self.blog_id, self.creator,))[0]
            Database.query_with_params(Sql.EDIT_COMMENT.value, (new_content, comment_id,))
            return True

        except Exception as exc:
            GeneralLogger.error(exc, COMMENT_LOG_FILE)

    def remove_content(self) -> Union[bool, None]:
        """
        Method to remove content of the comments
        """
        try:
            comment_to_remove = Database.get_item(Sql.GET_COMMENT_ID.value, (self.blog_id, self.creator))
            Database.remove_item(Sql.REMOVE_COMMENT_BY_ID.value, (comment_to_remove,))
            return True

        except Exception as exc:
            GeneralLogger.error(exc, COMMENT_LOG_FILE)

    def upvote(self, user_id: str) -> Union[bool, None]:
        """
        Method to upvote the comments
        """
        try:
            upvote_record = Database.get_item(Sql.CHECK_COMMENT_UPVOTE.value, (user_id, self.comment_id,))

            if upvote_record is None:
                self.upvotes += 1
                Database.insert_item(Sql.ADD_COMMENT_UPVOTE.value, (user_id, self.comment_id,))
                Database.query_with_params(Sql.UPDATE_COMMENT_UPVOTE.value, (self.upvotes, self.comment_id,))

                return True

            else:
                return False

        except Exception as exc:
            GeneralLogger.error(exc, COMMENT_LOG_FILE)

    def details(self) -> str:
        """
        Method to get details of the comments
        """
        comment_info = (self.creator, self.content, self.creation_date)

        return prompts.COMMENT_INFO.format(*comment_info)
