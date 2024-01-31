from models.database import Database
from config.sql_query_mysql import Sql
from models.comment_response import CommentResponse
from typing import Union, List


class GetCommentHandler:
    @staticmethod
    def get_comments_by_blog_id(blog_id) -> Union[None, List]:
        comments = Database.get_items(Sql.GET_COMMENT_BY_BLOG_ID.value, (blog_id,))
        if comments is None:
            return None
        comments = [CommentResponse(comment).to_dict() for comment in comments]
        return comments
