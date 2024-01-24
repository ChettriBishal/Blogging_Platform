import hashlib


class HashPassword:
    """This contains the method for hashing password"""
    @staticmethod
    def hash_password(password: str) -> str:
        """
        Method for hashing the password entered by the user
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password
