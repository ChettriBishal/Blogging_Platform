from dataclasses import dataclass


@dataclass
class CustomException(Exception):
    code: int
    message: str

    def dump(self):
        return {
            "code": self.code,
            "message": self.message
        }


class DoesNotExist(CustomException):
    pass


class AlreadyExists(CustomException):
    pass


class DbException(CustomException):
    pass
