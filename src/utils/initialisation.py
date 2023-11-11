from src.common.sql_query import Sql
from src.models import database

database.single_query(Sql.CREATE_USER_TABLE.value)
database.single_query(Sql.CREATE_POST_TABLE.value)
