from cerberus import Validator
from flask import request as FlaskRequest

from src.erros.types import HttpUnprocessableEntityError


def user_finder_validator(request: FlaskRequest):
    user_query_schema = {
        'first_name': {'required': True, 'type': 'string', 'empty': False}
    }
    v = Validator(user_query_schema)
    response = v.validate(request.args)

    if response is False:
        raise HttpUnprocessableEntityError(v.errors)
