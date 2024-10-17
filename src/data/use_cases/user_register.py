from datetime import date

from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.user_register import (
    UserRegister as UserRegisterInterface,
)


class UserRegister(UserRegisterInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def register(
        self, first_name: str, last_name: str, birth_date: date
    ) -> dict:
        self.__validate_name(first_name)

        self.__validate_name(last_name)

        self.__validate_birth_date(birth_date)

        self.__registry_user(first_name, last_name, birth_date)

        response = self.__format_respond(first_name, last_name, birth_date)

        return response

    @classmethod
    def __validate_name(cls, name: str) -> None:
        NAME_MAX_LENGHT = 18

        if not name.isalpha():
            raise Exception('Invalid characteres on name')

        if len(name) > NAME_MAX_LENGHT:
            raise Exception('Name exceed the 18 characteres maximum lenght')

    @classmethod
    def __validate_birth_date(cls, birth_date: date):
        if birth_date > date.today():
            raise Exception('Birth date cannot be in the future')

    def __registry_user(
        self, first_name: str, last_name: str, birth_date: date
    ) -> int:
        inserted_user_id = self.__users_repository.insert_user(
            first_name, last_name, birth_date
        )

        if inserted_user_id is None:
            raise Exception('Cannot insert user on database')

        return inserted_user_id

    @classmethod
    def __format_respond(
        cls, first_name: str, last_name: str, birth_date: date
    ) -> dict:
        attributes = {
            'first_name': first_name,
            'last_name': last_name,
            'birth_date': birth_date,
        }

        return {'type': 'Users', 'count': 1, 'attributes': attributes}
