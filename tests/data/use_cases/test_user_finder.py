import pytest

from src.data.use_cases.user_finder import UserFinder
from tests.infra.db.repositories.users_repository_spy import UsersRepositorySpy


def test_find():
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)
    first_name = 'John'
    users = user_finder.find(first_name)

    assert repo.get_user_by_first_name_params['first_name'] == first_name
    assert users['type'] == 'Users'
    assert len(users['attributes']) == users['count']
    assert users['attributes'] is not None


def test_find_invalid_alpha_first_name():
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)
    first_name = 'John123'  # Must be alphabetic
    with pytest.raises(Exception, match='Invalid first name to find'):
        user_finder.find(first_name)


def test_find_invalid_lenght_first_name():
    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)
    first_name = (
        'JohnDoeDoeDoeDoeFooBar'  # Exceed the 18 characteres maximum lenght
    )
    with pytest.raises(
        Exception, match='First name exceed the 18 characteres maximum lenght'
    ):
        user_finder.find(first_name)


def test_find_invalid_user_not_found():
    class UsersRepositoryError(UsersRepositorySpy):
        def get_user_by_first_name(self, first_name):
            return []

    repo = UsersRepositoryError()
    user_finder = UserFinder(repo)
    first_name = 'John'  # Exceed the 18 characteres maximum lenght
    with pytest.raises(Exception, match='User dont find.'):
        user_finder.find(first_name)
