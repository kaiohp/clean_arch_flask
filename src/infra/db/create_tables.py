from src.infra.db.base import Base
from src.infra.db.connection import DBConnectionHandler
from src.models.users import Users  # noqa F401

db_connection = DBConnectionHandler()

Base.metadata.create_all(bind=db_connection.get_engine())
