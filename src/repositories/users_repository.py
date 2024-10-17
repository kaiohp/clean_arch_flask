from datetime import date

from src.infra.db.connection import DBConnectionHandler
from src.models.users import Users as UsersEntity


class UsersRepository:
    @classmethod
    def insert_user(cls, first_name: str, last_name: str, birth_date: date):
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
