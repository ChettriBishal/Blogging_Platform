"""This module is used to create the tables if not present"""

from typing import Union
from config.sql_query import Sql
from models.database import Database


def initialize() -> Union[bool, None]:
    """
    Invoke all the methods to create the tables
    """
    Database.single_query(Sql.CREATE_USER_TABLE.value)

    Database.single_query(Sql.CREATE_BLOG_TABLE.value)

    Database.single_query(Sql.CREATE_COMMENTS_TABLE.value)

    Database.single_query(Sql.CREATE_BLOG_UPVOTES_TABLE.value)

    Database.single_query(Sql.CREATE_COMMENT_UPVOTES_TABLE.value)

    return True
