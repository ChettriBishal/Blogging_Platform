from marshmallow import Schema, fields


class BlogSchema(Schema):
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    content = fields.Str(required=True)
    timestamp = fields.DateTime(format='%Y-%m-%dT%H:%M')
    tags = fields.List(fields.String(), missing=[])


class BlogPostSchema(Schema):
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    tag = fields.Str(required=False)
