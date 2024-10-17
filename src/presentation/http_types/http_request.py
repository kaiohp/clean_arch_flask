from typing import Optional


class HttpRequest:
    def __init__(  # noqa: PLR0913
        self,
        headers: Optional[dict] = None,
        body: Optional[dict] = None,
        query_params: Optional[dict] = None,
        path_params: Optional[dict] = None,
        url: Optional[str] = None,
        ipv4: Optional[str] = None,
    ) -> None:
        self.headers = headers
        self.body = body
        self.query_params = query_params
        self.path_params = path_params
        self.url = url
        self.ipv4 = ipv4
