from src.common.sql_query import Sql
from src.utils import database
from src.loggers.general_logger import GeneralLogger
from src.common import filepaths


class User:
    def __init__(self, *user_info):
        (
            # receive user_id from the database itself
            self.username,
            self.password,
            self.user_role,
            self.email,
            self.registration_date,
        ) = user_info

        self.user_info = user_info
        self.user_id = None

    def get_details(self):
        return {
            'username': self.username,
            'role': self.user_role,
            'email': self.email,
            'registration_date': self.registration_date,
        }

    def add(self):
        try:
            self.user_id = database.insert_item(Sql.INSERT_USER.value, self.user_info)
            return True

        except Exception as exc:
            GeneralLogger.error(exc, filepaths.USER_LOG_FILE)
            return False

    def set_user_id(self, user_id):
        self.user_id = user_id

    def remove_user_by_username(self):
        try:
            database.remove_item(Sql.REMOVE_USER_BY_USERNAME.value, (self.username,))
            return True

        except Exception as exc:
            GeneralLogger.error(exc, filepaths.USER_LOG_FILE)
            return False

    def change_password(self, new_password):
        try:
            database.insert_item(Sql.UPDATE_PASSWORD.value, (new_password, self.username))
            return True

        except Exception as exc:
            GeneralLogger.error(exc, filepaths.USER_LOG_FILE)
            return False


