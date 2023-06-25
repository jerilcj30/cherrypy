from marshmallow import Schema, fields

class RequestDto(Schema):
    name = fields.Str(required=True)
    country = fields.Str(required=True)
    age = fields.Float(required=True)
    base_salary = fields.Float(required=True)
