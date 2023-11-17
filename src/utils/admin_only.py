from functools import wraps
from src.common.roles import Role
from src.common.prompts import ONLY_ADMIN


def admin(func):
    wraps(func)

    def wrapper(current_user):
        if current_user.user_role == Role.ADMIN.value:
            return func(current_user)
        else:
            raise PermissionError(ONLY_ADMIN)

    return wrapper
