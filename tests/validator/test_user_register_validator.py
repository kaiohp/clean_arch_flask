from datetime import date

import pytest

from src.erros.types import HttpUnprocessableEntityError
from src.validator.user_register_validator import user_register_validator


class MockFlaskRequest:
    def __init__(self):
        self.json: dict


def test_user_register_validator():
    request = MockFlaskRequest()
    request.json = {
        'first_name': 'Jon',
        'last_name': 'Snow',
        'birth_date': date(2010, 1, 1),
    }

    user_register_validator(request)


def test_user_register_validator_invalid_birth_date():
    request = MockFlaskRequest()
    request.json = {
        'first_name': 'Jon',
        'last_name': 'Snow',
        'birth_date': '2010-01-01',
    }

    with pytest.raises(HttpUnprocessableEntityError):
        user_register_validator(request)


def test_user_register_validator_missing_first_name():
    request = MockFlaskRequest()
    request.json = {
        'first_nome': 'Jon',
        'last_name': 'Snow',
        'birth_date': date(2010, 1, 1),
    }

    with pytest.raises(HttpUnprocessableEntityError):
        user_register_validator(request)
