from http import HTTPStatus

from src.presentation.controllers.user_finder_controller import (
    UserFinderController,
)
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from tests.data.use_cases.user_finder_spy import UserFinderSpy


class HttpRequestMock(HttpRequest):
    def __init__(self) -> None:
        query_params = {'first_name': 'Jon'}

        super().__init__(query_params=query_params)


def test_user_finder_controller():
    http_request_mock = HttpRequestMock()
    use_case = UserFinderSpy()
    user_finder_controller = UserFinderController(use_case)
    response = user_finder_controller.handle(http_request_mock)

    assert isinstance(response, HttpResponse)
    assert (
        use_case.find_params['first_name']
        == http_request_mock.query_params['first_name']
    )
    assert response.status_code == HTTPStatus.OK
    assert response.body['data'] is not None
