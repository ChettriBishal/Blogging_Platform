from models.database import Database
from config.sql_query_mysql import Sql
from models.comments.comment_response import CommentResponse
from typing import Union, List


class GetCommentHandler:
    @staticmethod
    def get_comments_by_blog_id(blog_id) -> Union[None, List]:
        """Get all comments for a specific blog"""
        comments = Database.get_items(Sql.GET_COMMENT_BY_BLOG_ID.value, (blog_id,))
        if comments is None:
            return None
        comments = [CommentResponse(comment).to_dict() for comment in comments]
        return comments

    @staticmethod
    def get_comment_by_comment_id(blog_id, comment_id):
        """Get a specific comment for a specific blog"""
        comment = Database.get_item(Sql.GET_SPECIFIC_COMMENT.value, (blog_id, comment_id))
        if comment is None:
            return None
        return CommentResponse(comment).to_dict()
