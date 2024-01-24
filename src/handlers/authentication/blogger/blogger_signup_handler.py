import hashlib
from datetime import datetime
from typing import Tuple, Union

from controllers.user import User
from config.roles import Role
from config.flags import Flag
from utils import validation
from models.database import Database
from config.sql_query_mysql import Sql


class BloggerSignUpHandler:
    @staticmethod
    def check_user_presence(username, email) -> bool:
        """This checks if user by username or/email is already present in the platform"""
        pass

    @staticmethod
    def create_user_object(username, password, email):
        """This creates a user object which interacts with the database"""
        pass
