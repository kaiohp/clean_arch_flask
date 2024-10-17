from http import HTTPStatus

from src.domain.use_cases.user_register import (
    UserRegister as UserRegisterInterface,
)
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import (
    ControllerInterface,
)


class UserRegistryController(ControllerInterface):
    def __init__(self, use_case: UserRegisterInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.body['first_name']
        last_name = http_request.body['last_name']
        birth_date = http_request.body['birth_date']

        response = self.__use_case.register(first_name, last_name, birth_date)

        return HttpResponse(
            status_code=HTTPStatus.CREATED, body={'data': response}
        )
