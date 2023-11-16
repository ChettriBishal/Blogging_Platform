import sqlite3

from src.common.filepaths import BLOGGING_DB
from src.loggers.general_logger import GeneralLogger
from src.common import filepaths


class DBConnection:
    def __init__(self):
        self.connection = None
        self.host = BLOGGING_DB
        self.cursor = None

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        self.cursor = self.connection.cursor()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_val}")
            print(f"Exception traceback: {exc_tb}")
            self.connection.close()

        else:
            self.connection.commit()
            self.connection.close()


def get_item(query, data):
    with DBConnection() as cursor:
        try:
            response = cursor.execute(query, data).fetchone()
            return response

        except sqlite3.Error as error:
            GeneralLogger.error(error, filepaths.DB_LOG_FILE)


def get_items(query, data=None):
    with DBConnection() as cursor:
        try:
            if data is None:
                response = cursor.execute(query).fetchall()
            else:
                response = cursor.execute(query, data).fetchall()

            return response

        except sqlite3.Error as error:
            GeneralLogger.error(error, filepaths.DB_LOG_FILE)


def insert_item(query, data):
    with DBConnection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(query, data)
            return cursor.lastrowid

        except sqlite3.Error as error:
            GeneralLogger.error(error, filepaths.DB_LOG_FILE)


def remove_item(query, data):
    with DBConnection() as cursor:
        try:
            cursor.execute(query, data)

        except sqlite3.Error as error:
            GeneralLogger.error(error, filepaths.DB_LOG_FILE)


def single_query(query):
    with DBConnection() as cursor:
        try:
            cursor.execute(query)

        except sqlite3.Error as error:
            GeneralLogger.error(error, filepaths.DB_LOG_FILE)


def query_with_params(query, data):
    with DBConnection() as cursor:
        try:
            cursor.execute(query, data)

        except sqlite3.Error as error:
            GeneralLogger.error(error, filepaths.DB_LOG_FILE)
