from src.common.sql_query import SQL
from src.models import database

database.single_query(SQL.CREATE_USER_TABLE.value)
database.single_query(SQL.CREATE_POST_TABLE.value)
