import re


def validate_username(username):
    pattern = '^[a-zA-Z0-9_]+$'
    matcher = re.match(pattern, username)
    return matcher


def validate_password(password):
    pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    matcher = re.match(pattern, password)
    return matcher


def validate_email(email):
    pattern = '^[a-zA-Z][a-zA-Z0-9]+\@[a-zA-Z]+\.(in|net|com)'
    matcher = re.match(pattern, email)
    return matcher
