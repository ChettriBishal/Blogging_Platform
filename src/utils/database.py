import sqlite3

from src.loggers.general_logger import GeneralLogger
from src.common import filepaths
from src.models.db_connection import DBConnection

blog_db_connection = DBConnection()


def get_item(query, data):
    with blog_db_connection as cursor:
        try:
            response = cursor.execute(query, data).fetchone()
            return response

        except sqlite3.Error as error:
            GeneralLogger.error(error, filepaths.DB_LOG_FILE)


def get_items(query, data=None):
    with blog_db_connection as cursor:
        try:
            if data is None:
                response = cursor.execute(query).fetchall()
            else:
                response = cursor.execute(query, data).fetchall()

            return response

        except sqlite3.Error as error:
            GeneralLogger.error(error, filepaths.DB_LOG_FILE)


def insert_item(query, data):
    with blog_db_connection as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(query, data)
            return cursor.lastrowid

        except sqlite3.Error as error:
            GeneralLogger.error(error, filepaths.DB_LOG_FILE)


def remove_item(query, data):
    with blog_db_connection as cursor:
        try:
            cursor.execute(query, data)

        except sqlite3.Error as error:
            GeneralLogger.error(error, filepaths.DB_LOG_FILE)


def single_query(query):
    with blog_db_connection as cursor:
        try:
            cursor.execute(query)

        except sqlite3.Error as error:
            GeneralLogger.error(error, filepaths.DB_LOG_FILE)


def query_with_params(query, data):
    with blog_db_connection as cursor:
        try:
            cursor.execute(query, data)

        except sqlite3.Error as error:
            GeneralLogger.error(error, filepaths.DB_LOG_FILE)
