from handlers.authentication.user.blocklist import BLOCKLIST
from models.database import Database


class LogoutHandler:
    @staticmethod
    def logout(jti):
        """Add jti to the BLOCKLIST set"""
        # make the db call to add this to the blocklist
        BLOCKLIST.add(jti)
