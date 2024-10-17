from cerberus import Validator
from flask import request as FlaskRequest

from src.erros.types import HttpUnprocessableEntityError


def user_register_validator(request: FlaskRequest):
    user_body_schema = {
        'first_name': {'required': True, 'type': 'string', 'empty': False},
        'last_name': {'required': True, 'type': 'string', 'empty': False},
        'birth_date': {'required': True, 'type': 'date', 'empty': False},
    }
    v = Validator(user_body_schema)
    response = v.validate(request.json)

    if response is False:
        raise HttpUnprocessableEntityError(v.errors)
