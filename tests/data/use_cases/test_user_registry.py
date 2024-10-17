from datetime import date, timedelta

import pytest

from src.data.use_cases.user_register import UserRegister
from tests.infra.db.repositories.users_repository_spy import UsersRepositorySpy


def test_register():
    first_name = 'Jon'
    last_name = 'Doe'
    birth_date = date(2001, 1, 1)

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    response = user_register.register(first_name, last_name, birth_date)

    assert repo.insert_user_params['first_name'] == first_name
    assert repo.insert_user_params['last_name'] == last_name
    assert repo.insert_user_params['birth_date'] == birth_date

    assert response['type'] == 'Users'
    assert response['count'] == 1
    assert response['attributes'] is not None


def test_register_invalid_alpha_first_name():
    first_name = 'Jon123'
    last_name = 'Doe'
    birth_date = date(2001, 1, 1)

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    with pytest.raises(Exception, match='Invalid characteres on name'):
        user_register.register(first_name, last_name, birth_date)


def test_register_invalid_alpha_last_name():
    first_name = 'Jon'
    last_name = 'Doe123'
    birth_date = date(2001, 1, 1)

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    with pytest.raises(Exception, match='Invalid characteres on name'):
        user_register.register(first_name, last_name, birth_date)


def test_register_invalid_lenght_first_name():
    first_name = 'JonDoeDoeDoeDoeFooBar'
    last_name = 'Doe'
    birth_date = date(2001, 1, 1)

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    with pytest.raises(
        Exception, match='Name exceed the 18 characteres maximum lenght'
    ):
        user_register.register(first_name, last_name, birth_date)


def test_register_invalid_lenght_last_name():
    first_name = 'Jon'
    last_name = 'DoeDoeDoeDoeDoeFooBar'
    birth_date = date(2001, 1, 1)

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    with pytest.raises(
        Exception, match='Name exceed the 18 characteres maximum lenght'
    ):
        user_register.register(first_name, last_name, birth_date)


def test_register_invalid_date():
    first_name = 'Jon'
    last_name = 'Doe'
    birth_date = date.today() + timedelta(1)

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    with pytest.raises(Exception, match='Birth date cannot be in the future'):
        user_register.register(first_name, last_name, birth_date)
