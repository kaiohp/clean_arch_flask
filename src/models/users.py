from sqlalchemy import Column, Date, Integer, String

from src.infra.db.base import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)

    def __repr__(self):
        return (
            f'User(id={self.id}, first_name={self.first_name},'
            f'last_name={self.last_name}, birth_date={self.birth_date})'
        )
