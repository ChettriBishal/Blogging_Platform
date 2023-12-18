"""This module is for validating the inputs entered by the user"""

import re
from typing import Optional


def validate_username(username: str) -> bool:
    """
    This function validates the username entered by the user
    """
    pattern = '^(?=.*[a-zA-Z])[a-zA-Z0-9_]+$'
    matcher = re.match(pattern, username)

    return bool(matcher)


def validate_password(password) -> Optional[re.Match]:
    """
    This function validates the password
    """
    pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    matcher = re.match(pattern, password)

    return matcher


def validate_email(email) -> Optional[re.Match]:
    """
    This function validates the email entered by the user
    """
    pattern = '^[a-zA-Z][a-zA-Z0-9]+\@[a-zA-Z]+\.(in|net|com)'
    matcher = re.match(pattern, email)

    return matcher


def validate_empty_input(text) -> Optional[re.Match, bool]:
    """
    This function checks for empty input entered by the user
    """
    pattern = r'^\s*$'

    return re.match(pattern, text) is not None
