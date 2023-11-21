import sqlite3

from src.config.filepaths import BLOGGING_DB


class DBConnection:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.connection = None
            cls._instance.host = BLOGGING_DB
            cls._instance.cursor = None

        return cls._instance

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.host)
        self.cursor = self.connection.cursor()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_val}")
            print(f"Exception traceback: {exc_tb}")

        else:
            self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()
