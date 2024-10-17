from http import HTTPStatus


class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        self.name = 'Unprocessable Entity'
        self.status_code = HTTPStatus.UNPROCESSABLE_ENTITY
