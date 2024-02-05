from handlers.authentication.user.blocklist import BLOCKLIST


class LogoutHandler:
    @staticmethod
    def logout(jti):
        """Add jti to the BLOCKLIST set"""
        BLOCKLIST.add(jti)
