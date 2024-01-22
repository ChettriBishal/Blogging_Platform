from marshmallow import fields, Schema


class ResponseSchema(Schema):
    status = fields.Integer(required=True, example=200)
    response_message = fields.String(required=True)
    errors = fields.List(fields.Dict(), missing=[])
    data = fields.Dict(required=True)
