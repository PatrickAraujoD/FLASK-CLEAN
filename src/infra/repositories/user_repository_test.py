from faker import Faker
from sqlalchemy import text
from src.infra.config import BDConnectionHandler
from .user_repository import UserRepository
from src.infra.entities import Users as UsersModel

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


def testSelectUser():
    """Should select a user in Users table and compare it"""
    userId = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()
    data = UsersModel(id=userId, name=name, password=password)

    engine = connection.getEngine()

    with engine.connect() as conn:
        query = text(
            f"INSERT INTO users(id, name, password) VALUES (:id, :name, :password)"
        )
        conn.execute(query, {"id": userId, "name": name, "password": password})
        conn.commit()

    queryUser = userRepository.selectUser(userId=userId)
    queryUser2 = userRepository.selectUser(name=name)
    queryUser3 = userRepository.selectUser(userId=userId, name=name)
    print(data in queryUser)
    assert data in queryUser
    assert data in queryUser2
    assert data in queryUser3

    with engine.connect() as conn:
        query = text(f"DELETE FROM users WHERE id=:id")
        conn.execute(query, {"id": userId})
        conn.commit()
