from datetime import date

from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.infra.db.connection import DBConnectionHandler
from src.infra.db.models.users import Users as UsersEntity


class UsersRepository(UsersRepositoryInterface):
    @classmethod
    def insert_user(
        cls, first_name: str, last_name: str, birth_date: date
    ) -> int:
        with DBConnectionHandler() as session:
            try:
                new_user = UsersEntity(
                    first_name=first_name,
                    last_name=last_name,
                    birth_date=birth_date,
                )

                session.add(new_user)
                session.commit()
                return new_user.id
            except Exception as exception:
                session.rollback()
                raise exception

    @classmethod
    def get_user_by_first_name(cls, first_name: str) -> list[UsersEntity]:
        with DBConnectionHandler() as session:
            try:
                users = (
                    session.query(UsersEntity)
                    .filter(UsersEntity.first_name == first_name)
                    .all()
                )
                return users
            except Exception as exception:
                session.rollback()
                raise exception
