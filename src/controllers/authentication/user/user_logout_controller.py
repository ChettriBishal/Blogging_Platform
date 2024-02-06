from handlers.authentication.user.user_logout_handler import LogoutHandler
from config.message import Message
from utils.exceptions import DbException


class LogoutController:
    @staticmethod
    def logout(token):
        """To add the current user in BLOCKLIST"""
        try:
            LogoutHandler.logout()
            return {"message": Message.LOGGED_OUT}
        except DbException as exc:
            return exc.dump()
