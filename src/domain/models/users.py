from datetime import date


class Users:
    def __init__(
        self, id: int, first_name: str, last_name: str, birth_date: date
    ) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
