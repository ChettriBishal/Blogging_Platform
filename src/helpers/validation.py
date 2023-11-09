import re


def validate_username(username):
    pattern = '[A-Za-Z1-9_]+'
    matcher = re.fullmatch(pattern, username)
    return matcher


def validate_password(password):
    pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    matcher = re.fullmatch(pattern, password)
    return matcher


def validate_email(email):
    pattern = '^[a-zA-Z][a-zA-Z0-9]+\@[a-zA-Z]+\.(in|net|com)'
    matcher = re.fullmatch(pattern, email)
    return matcher
