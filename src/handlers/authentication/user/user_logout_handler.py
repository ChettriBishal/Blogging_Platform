from models.database import Database
from flask_jwt_extended import get_jwt
from utils.tokens.token import Token
from utils.exceptions import DbException


class LogoutHandler:
    @staticmethod
    def logout():
        """Add jti to tokens db and set the status as revoked"""
        # make the db call to add this to the blocklist
        try:
            Token.revoke_token(get_jwt())
        except DbException:
            raise DbException

