from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.usecases.user_finder import UserFinder as UserFinderInterface


class UserFinder(UserFinderInterface):
    FIRST_NAME_MAX_LENGHT = 18

    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> dict:
        if not first_name.isalpha():
            raise Exception('Invalid first name to find')

        if len(first_name) > UserFinder.FIRST_NAME_MAX_LENGHT:
            raise Exception(
                'First name exceed the 18 characteres maximo lenght'
            )

        users = self.__users_repository.get_user_by_first_name(first_name)

        if not users:
            raise Exception('User dont find.')

        response = {'type': 'Users', 'count': len(users), 'attributes': users}

        return response
