from abc import ABC, abstractmethod
from datetime import date

from src.domain.models.users import Users


class UsersRepositoryInterface(ABC):
    @abstractmethod
    def insert_user(
        self, first_name: str, last_name: str, birth_date: date
    ) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_user_by_first_name(self, first_name: str) -> list[Users]:
        raise NotImplementedError
