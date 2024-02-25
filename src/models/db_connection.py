"""This module defines how db connection is created"""
import os
import mysql.connector
import pymysql


class DBConnection:
    """
    This class contains methods to create a db context manager with singleton approach
    """
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.connection = None
            cls._instance.host = os.getenv('DB_NAME')
            cls._instance.cursor = None

        return cls._instance

    def __enter__(self):
        """
        Setup operations when context manager is opened
        """
        # self.connection = sqlite3.connect(self.host)

        # self.connection = mysql.connector.connect(
        #     host=os.getenv('DB_HOST'),
        #     user=os.getenv('DB_USERNAME'),
        #     password=os.getenv('DB_PASSWORD'),
        #     database=os.getenv('DB_NAME')
        # )
        self.connection = pymysql.connect(
            port=int(os.getenv('DB_PORT')),
            cursorclass=pymysql.cursors.DictCursor,
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            db=os.getenv('DB_NAME'),
        )

        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Operations when the context manager is closed
        """
        if exc_type or exc_val or exc_tb:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_val}")
            print(f"Exception traceback: {exc_tb}")

        else:
            self.connection.commit()
            self.connection.close()

    def close(self) -> None:
        """
        Explicitly close the database connection
        """
        if self.connection:
            self.connection.close()

# class DBConnection:
#     def __init__(self):
#         self.connection = mysql.connector.connect(
#             host='localhost',
#             user=os.getenv('DB_USERNAME'),
#             password=os.getenv('DB_PASSWORD'),
#             database=os.getenv('DB_NAME')
#         )
#
#     def __enter__(self):
#         return self.connection
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type or exc_tb or exc_val:
#             return False
#         self.connection.commit()
#         self.connection.close()
