from http import HTTPStatus


class HttpInternalServerError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        self.name = 'Internal Server Error'
        self.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
