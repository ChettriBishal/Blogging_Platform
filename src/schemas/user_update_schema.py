from marshmallow import Schema, fields


class UserUpdateSchema(Schema):
    password = fields.String(required=False)
    email = fields.String(required=False)
