from marshmallow import Schema, fields, validate
from config.regex_patterns import username_regex, password_regex, email_regex


class SignUpSchema(Schema):
    username = fields.String(required=True, validate=validate.Regexp(username_regex))
    password = fields.String(required=True, load_only=True, validate=password_regex)
    email = fields.String(required=True, validate=email_regex)


class LoginSchema(Schema):
    username = fields.String(required=True, validate=validate.Regexp(username_regex))
    password = fields.String(required=True, load_only=True, validate=password_regex)
