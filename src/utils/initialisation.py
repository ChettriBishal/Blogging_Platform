from src.common.sql_query import Sql
from src.controllers.database import Database


def initialize():
    Database.single_query(Sql.CREATE_USER_TABLE.value)

    Database.single_query(Sql.CREATE_BLOG_TABLE.value)

    Database.single_query(Sql.CREATE_COMMENTS_TABLE.value)

    Database.single_query(Sql.CREATE_BLOG_UPVOTES_TABLE.value)

    Database.single_query(Sql.CREATE_COMMENT_UPVOTES_TABLE.value)
