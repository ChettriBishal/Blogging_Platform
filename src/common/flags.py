from enum import Enum


class Flag(Enum):
    DOES_NOT_EXIST = -1
    INVALID_EMAIL = -2
    INVALID_PASSWORD = -3
    INVALID_USERNAME = -4
    ALREADY_EXISTS = -5
    EMPTY_INPUT = -6
