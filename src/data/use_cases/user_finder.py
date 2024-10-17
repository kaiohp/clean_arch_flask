from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.erros.types import HttpBadRequestError, HttpNotFoundError


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> dict:
        self.__validate_first_name(first_name)

        users = self.__search_user_by_first_name(first_name)

        response = self.__format_response(users)

        return response

    @classmethod
    def __validate_first_name(cls, first_name: str) -> None:
        FIRST_NAME_MAX_LENGHT = 18

        if not first_name.isalpha():
            raise HttpBadRequestError('Invalid first name to find')

        if len(first_name) > FIRST_NAME_MAX_LENGHT:
            raise HttpBadRequestError(
                'First name exceed the 18 characteres maximum lenght'
            )

    def __search_user_by_first_name(self, first_name: str) -> list:
        users = self.__users_repository.get_user_by_first_name(first_name)
        if not users:
            raise HttpNotFoundError('User dont find.')
        return users

    @classmethod
    def __format_response(cls, users: list[Users]) -> dict:
        attributes = []
        for user in users:
            record = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'birth_date': user.birth_date,
            }
            attributes.append(record)
        return {'type': 'Users', 'count': len(users), 'attributes': attributes}
