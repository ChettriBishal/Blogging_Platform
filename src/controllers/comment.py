from src.controllers.post import Post
from src.config.sql_query import Sql
from src.models.database import Database
from src.config import prompts
from src.loggers.general_logger import GeneralLogger
from src.config.filepaths import COMMENT_LOG_FILE


class Comment(Post):
    def __init__(self, comment_info):
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

    def add_content(self):
        try:
            self.comment_id = Database.insert_item(Sql.INSERT_COMMENT.value, self.comment_info)
            if self.comment_id:
                return True

        except Exception as exc:
            GeneralLogger.error(exc, COMMENT_LOG_FILE)

    def edit_content(self, new_content):
        try:
            comment_id = Database.get_item(Sql.GET_COMMENT_ID.value, (self.blog_id, self.creator,))[0]
            Database.query_with_params(Sql.EDIT_COMMENT.value, (new_content, comment_id,))
            return True

        except Exception as exc:
            GeneralLogger.error(exc, COMMENT_LOG_FILE)

    def remove_content(self):
        try:
            comment_to_remove = Database.get_item(Sql.GET_COMMENT_ID.value, (self.blog_id, self.creator))
            Database.remove_item(Sql.REMOVE_COMMENT_BY_ID.value, (comment_to_remove,))
            return True

        except Exception as exc:
            GeneralLogger.error(exc, COMMENT_LOG_FILE)

    def upvote(self, user_id):
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

    def details(self):
        comment_info = (self.creator, self.content, self.creation_date)

        return prompts.COMMENT_INFO.format(*comment_info)
