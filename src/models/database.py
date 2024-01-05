"""This module defines the various database operations"""

import sqlite3
from typing import Any, Optional, Tuple, List

from loggers.general_logger import GeneralLogger
from config import filepaths
from models.db_connection import DBConnection


class Database:
    """
    This class contains methods for accessing and altering the database
    """
    blog_db_connection = DBConnection()

    @classmethod
    def get_item(cls, query: str, data: Any) -> Optional[Tuple]:
        """
        This method fetches a single item from the database
        """
        with cls.blog_db_connection as cursor:
            try:
                response = cursor.execute(query, data).fetchone()
                return response

            except sqlite3.Error as error:
                GeneralLogger.error(error, filepaths.DB_LOG_FILE)

    @classmethod
    def get_items(cls, query: str, data=None) -> Optional[List]:
        """
        This method fetches many items from the database
        """
        with cls.blog_db_connection as cursor:
            try:
                if data is None:
                    response = cursor.execute(query).fetchall()
                else:
                    response = cursor.execute(query, data).fetchall()

                return response

            except sqlite3.Error as error:
                GeneralLogger.error(error, filepaths.DB_LOG_FILE)
                return None

    @classmethod
    def insert_item(cls, query: str, data: Any) -> Optional[int]:
        """
        This method allows data to be inserted into the database
        """
        with cls.blog_db_connection as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query, data)
                return cursor.lastrowid

            except sqlite3.Error as error:
                GeneralLogger.error(error, filepaths.DB_LOG_FILE)
                return None

    @classmethod
    def remove_item(cls, query: str, data: Any) -> Optional[None]:
        """
        This method allows data to be removed from a database
        """
        with cls.blog_db_connection as cursor:
            try:
                cursor.execute(query, data)

            except sqlite3.Error as error:
                GeneralLogger.error(error, filepaths.DB_LOG_FILE)
                return None

    @classmethod
    def single_query(cls, query: str) -> Optional[None]:
        """
        This method defines a generic query with no conditions
        """
        with cls.blog_db_connection as cursor:
            try:
                cursor.execute(query)

            except sqlite3.Error as error:
                GeneralLogger.error(error, filepaths.DB_LOG_FILE)
                return None

    @classmethod
    def query_with_params(cls, query: str, data: Any) -> Optional[None]:
        """
        This method defines a generic query with conditions
        """
        with cls.blog_db_connection as cursor:
            try:
                cursor.execute(query, data)

            except sqlite3.Error as error:
                GeneralLogger.error(error, filepaths.DB_LOG_FILE)
                return None
