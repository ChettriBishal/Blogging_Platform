from handlers.authentication.user.user_logout_handler import LogoutHandler
from config.message import Message


class LogoutController:
    @staticmethod
    def logout(token):
        """To add the current user in BLOCKLIST"""
        jti = token.get('jti')
        LogoutHandler.logout(jti)
        return {"message": Message.LOGGED_OUT}
