from datetime import date

from src.infra.db.connection import DBConnectionHandler
from src.models.users import Users
from src.repositories.users_repository import UsersRepository


def test_insert_user():
    mocked_first_name = 'John'
    mocked_last_name = 'Doe'
    mocked_birth_date = date(2000, 1, 1)

    mocked_user_id = UsersRepository.insert_user(
        first_name=mocked_first_name,
        last_name=mocked_last_name,
        birth_date=mocked_birth_date,
    )

    with DBConnectionHandler() as session:
        inserted_user = session.get(Users, mocked_user_id)

        session.delete(inserted_user)
        session.commit()

        assert inserted_user.first_name == mocked_first_name
        assert inserted_user.last_name == mocked_last_name
        assert inserted_user.birth_date == mocked_birth_date


def test_get_user_by_first_name():
    mocked_first_name = 'John'
    mocked_last_name = 'Doe'
    mocked_birth_date = date(2000, 1, 1)

    with DBConnectionHandler() as session:
        session.add(
            Users(
                first_name=mocked_first_name,
                last_name=mocked_last_name,
                birth_date=mocked_birth_date,
            )
        )
        session.commit()

    users = UsersRepository.get_user_by_first_name(
        first_name=mocked_first_name
    )

    with DBConnectionHandler() as session:
        for user in users:
            session.delete(user)
        session.commit()

    assert len(users) == 1
    assert users[0].first_name == mocked_first_name
    assert users[0].last_name == mocked_last_name
    assert users[0].birth_date == mocked_birth_date
