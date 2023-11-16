from src.controllers.post import Post
from src.common.sql_query import Sql
from src.models import database
from src.common import prompts


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
            self.comment_id = database.insert_item(Sql.INSERT_COMMENT.value, self.comment_info)
            return True

        except Exception as exc:
            print(exc)

    def edit_content(self, new_content):
        try:
            comment_id = database.get_item(Sql.GET_COMMENT_ID.value, (self.blog_id, self.creator,))[0]
            database.query_with_params(Sql.EDIT_COMMENT.value, (new_content, comment_id,))
            return True

        except Exception as exc:
            print(exc)

    def remove_content(self):
        comment_to_remove = database.get_item(Sql.GET_COMMENT_ID.value, (self.blog_id, self.creator))
        try:
            database.remove_item(Sql.REMOVE_COMMENT_BY_ID.value, (comment_to_remove,))

        except Exception as exc:
            print(exc)

    def upvote(self, user_id):
        upvote_record = database.get_item(Sql.CHECK_COMMENT_UPVOTE.value, (user_id, self.comment_id,))

        if upvote_record is None:
            self.upvotes += 1
            database.insert_item(Sql.ADD_COMMENT_UPVOTE.value, (user_id, self.comment_id,))
            database.query_with_params(Sql.UPDATE_COMMENT_UPVOTE.value, (self.upvotes, self.comment_id,))
            return True

        else:
            return False

    def details(self):
        comment_info = (self.creator, self.content, self.creation_date)

        return prompts.COMMENT_INFO.format(*comment_info)



