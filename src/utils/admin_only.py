"""This module defines a decorator for admin access"""

from typing import Optional
from functools import wraps
from config.roles import Role
from config.prompts import ONLY_ADMIN
from controllers.user import User


def admin(func):
    """
    This decorator allows role based access to admin entity
    """
    @wraps(func)
    def wrapper(current_user: User) -> Optional[None]:
        if current_user.user_role == Role.ADMIN.value:
            return func(current_user)
        else:
            raise PermissionError(ONLY_ADMIN)

    return wrapper
