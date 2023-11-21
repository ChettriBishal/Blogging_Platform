import sqlite3

from src.loggers.general_logger import GeneralLogger
from src.config import filepaths
from src.models.db_connection import DBConnection


class Database:
    blog_db_connection = DBConnection()

    @classmethod
    def get_item(cls, query, data):
        with cls.blog_db_connection as cursor:
            try:
                response = cursor.execute(query, data).fetchone()
                return response

            except sqlite3.Error as error:
                GeneralLogger.error(error, filepaths.DB_LOG_FILE)

    @classmethod
    def get_items(cls, query, data=None):
        with cls.blog_db_connection as cursor:
            try:
                if data is None:
                    response = cursor.execute(query).fetchall()
                else:
                    response = cursor.execute(query, data).fetchall()

                return response

            except sqlite3.Error as error:
                GeneralLogger.error(error, filepaths.DB_LOG_FILE)

    @classmethod
    def insert_item(cls, query, data):
        with cls.blog_db_connection as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query, data)
                return cursor.lastrowid

            except sqlite3.Error as error:
                GeneralLogger.error(error, filepaths.DB_LOG_FILE)

    @classmethod
    def remove_item(cls, query, data):
        with cls.blog_db_connection as cursor:
            try:
                cursor.execute(query, data)

            except sqlite3.Error as error:
                GeneralLogger.error(error, filepaths.DB_LOG_FILE)

    @classmethod
    def single_query(cls, query):
        with cls.blog_db_connection as cursor:
            try:
                cursor.execute(query)

            except sqlite3.Error as error:
                GeneralLogger.error(error, filepaths.DB_LOG_FILE)

    @classmethod
    def query_with_params(cls, query, data):
        with cls.blog_db_connection as cursor:
            try:
                cursor.execute(query, data)

            except sqlite3.Error as error:
                GeneralLogger.error(error, filepaths.DB_LOG_FILE)
