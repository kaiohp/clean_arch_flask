from sqlalchemy import Engine

from src.infra.db.connection import DBConnectionHandler


def test_create_database_engine():
    db_connection = DBConnectionHandler()

    engine = db_connection.get_engine()
    conn = engine.connect()

    assert engine is not None
    assert isinstance(engine, Engine)
    assert not conn.closed

    conn.close()
