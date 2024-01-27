from config.sql_query_mysql import Sql
from models.database import Database


class UserInfoHandler:
    @staticmethod
    def get_user_id_by_username(username):
        userid = Database.get_item(Sql.GET_USER_ID_BY_USERNAME.value, (username,))
        return userid

    @staticmethod
    def get_username_by_userid(userid):
        username = Database.get_item(Sql.GET_USERNAME_BY_USERID.value, (userid,))
        return username
