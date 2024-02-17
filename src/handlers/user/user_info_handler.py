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

    @staticmethod
    def get_user_row_by_username(username):
        user_details = Database.get_item(Sql.GET_USER_ROW_BY_USERNAME.value, (username,))
        return user_details

    @staticmethod
    def get_all_users():
        users = Database.get_items(Sql.GET_ALL_USERS.value, None)
        return users

    @staticmethod
    def remove_user_by_username(username):
        Database.remove_item(Sql.REMOVE_USER_BY_USERNAME.value, (username,))

    @staticmethod
    def remove_user_by_userid(user_id):
        Database.remove_item(Sql.REMOVE_USER_BY_USERID.value, (user_id,))
