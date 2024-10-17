import pytest

from src.erros.types import HttpUnprocessableEntityError
from src.validator.user_finder_validator import user_finder_validator


class MockFlaskRequest:
    def __init__(self):
        self.args: dict


def test_user_finder_validator():
    request = MockFlaskRequest()
    request.args = {'first_name': 'Jon'}

    user_finder_validator(request)


def test_user_finder_validator_missing_query_params():
    request = MockFlaskRequest()
    request.args = {'first_nome': 'Jon'}

    with pytest.raises(HttpUnprocessableEntityError):
        user_finder_validator(request)


def test_user_finder_validator_invalid_query_params():
    request = MockFlaskRequest()
    request.args = {'first_name': 123}

    with pytest.raises(HttpUnprocessableEntityError):
        user_finder_validator(request)
