from faker import Faker
from src.infra.config import BDConnectionHandler
from .user_repository import UserRepository
from sqlalchemy import text

faker = Faker()
userRepository = UserRepository()
connection = BDConnectionHandler()


def testInsertUser():
    """Should Insert User"""
    name = faker.name()
    password = faker.word()
    engine = connection.getEngine()

    newUser = userRepository.insertUser(name, password)

    with engine.connect() as conn:
        query = text("SELECT * FROM users WHERE id=:user_id")
        result = conn.execute(query, {"user_id": newUser.id}).fetchone()

        query = text("DELETE FROM users WHERE id=:user_id")
        conn.execute(query, {"user_id": newUser.id})
        conn.commit()

    assert result is not None
    assert result.name == newUser.name
    assert result.password == newUser.password
