from dataclasses import dataclass


@dataclass
class CustomException(Exception):
    code: int
    error: str
    message: str

    def dump(self):
        return {
            "code": self.code,
            "error": self.error,
            "message": self.message
        }


class DoesNotExist(CustomException):
    pass


class AlreadyExists(CustomException):
    pass
