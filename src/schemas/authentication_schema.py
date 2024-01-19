from marshmallow import Schema, fields, validate
from config.regex_patterns import username_regex, password_regex, email_regex

class SignUpSchema(Schema):
    username = fields.Str(required=True, validate=validate.Regexp(username_regex))
    password = fields.Str(required=True, load_only=True, validate=password_regex)
    email = fields.Str(required=True, validate=email_regex)


class LoginSchema(Schema):
    username = fields.Str(required=True, validate=validate.Regexp(username_regex))
    password = fields.Str(required=True, load_only=True, validate=password_regex)
