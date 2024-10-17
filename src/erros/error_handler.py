from http import HTTPStatus

from src.erros.types import (
    HttpBadRequestError,
    HttpInternalServerError,
    HttpNotFoundError,
    HttpUnprocessableEntityError,
)
from src.presentation.http_types.http_response import HttpResponse


def handle_error(error: Exception) -> HttpResponse:
    if isinstance(
        error,
        (
            HttpBadRequestError,
            HttpNotFoundError,
            HttpInternalServerError,
            HttpUnprocessableEntityError,
        ),
    ):
        return HttpResponse(
            status_code=error.status_code,
            body={'errors': {'title': error.name, 'detail': error.message}},
        )

    return HttpResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        body={
            'errors': {'title': 'Internal Server Error', 'detail': str(error)}
        },
    )
