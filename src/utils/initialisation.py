from src.common.sql_query import Sql
from src.utils import database


def initialize():
    database.single_query(Sql.CREATE_USER_TABLE.value)

    database.single_query(Sql.CREATE_BLOG_TABLE.value)

    database.single_query(Sql.CREATE_COMMENTS_TABLE.value)

    database.single_query(Sql.CREATE_BLOG_UPVOTES_TABLE.value)

    database.single_query(Sql.CREATE_COMMENT_UPVOTES_TABLE.value)
