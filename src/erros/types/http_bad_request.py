from http import HTTPStatus


class HttpBadRequestError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        self.name = 'Bad Request'
        self.status_code = HTTPStatus.BAD_REQUEST
