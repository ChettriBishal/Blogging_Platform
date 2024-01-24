from .hash_password_util import HashPassword


class CheckPassword:
    """This checks if password entered is same against the hashed password"""
    @staticmethod
    def check_password(password: str, hashed_password: str) -> bool:
        """
        Method for validating the password against the stored password
        """
        if HashPassword.hash_password(password) == hashed_password:
            return True
        return False
