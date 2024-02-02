from models.database import Database
from config.sql_query_mysql import Sql


class CommentInfoHandler:
    @staticmethod
    def get_creator_id_for_comment(blog_id, comment_id):
        """Get creator ID for comment -> Comment writer"""
        creator_id = Database.get_item(Sql.GET_CREATOR_ID_FOR_COMMENT.value, (blog_id, comment_id,))[0]
        return creator_id
