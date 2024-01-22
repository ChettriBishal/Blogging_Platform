from marshmallow import Schema, fields


class CommentSchema(Schema):
    author = fields.String(required=True)
    content = fields.String(required=True)
    timestamp = fields.DateTime(format='%Y-%m-%dT%H:%M')
