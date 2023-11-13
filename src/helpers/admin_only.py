from functools import wraps
from src.common.roles import Role


def admin(func):
    wraps(func)

    def wrapper(current_user):
        if current_user.user_role == Role.ADMIN.value:
            return func(current_user)
        else:
            raise PermissionError("Admin privileges required for this operation")

    return wrapper
