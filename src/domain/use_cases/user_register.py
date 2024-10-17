from abc import ABC, abstractmethod
from datetime import date


class UserRegister(ABC):
    @abstractmethod
    def register(
        self, first_name: str, last_name: str, birth_date: date
    ) -> dict:
        raise NotImplementedError
