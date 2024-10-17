from datetime import date
from http import HTTPStatus

from src.presentation.controllers.user_registry_controller import (
    UserRegistryController,
)
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from tests.data.use_cases.user_registry_spy import UserRegisterSpy


class HttpResquetMock(HttpRequest):
    def __init__(self) -> None:
        body = {
            'first_name': 'Jon',
            'last_name': 'Doe',
            'birth_date': date(2000, 1, 1),
        }
        super().__init__(body=body)


def test_user_registry_controller():
    http_resquest_mock = HttpResquetMock()
    use_case = UserRegisterSpy()
    user_registry_controller = UserRegistryController(use_case)

    response = user_registry_controller.handle(http_resquest_mock)

    assert isinstance(response, HttpResponse)
    assert (
        use_case.register_params['first_name']
        == http_resquest_mock.body['first_name']
    )
    assert (
        use_case.register_params['last_name']
        == http_resquest_mock.body['last_name']
    )
    assert (
        use_case.register_params['birth_date']
        == http_resquest_mock.body['birth_date']
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.body['data'] is not None
