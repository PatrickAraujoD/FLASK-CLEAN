from collections import namedtuple
from src.infra.config import BDConnectionHandler
from src.infra.entities import Users


class UserRepository:
    @classmethod
    def insertUser(cls, name: str, password: str) -> Users:
        insertData = namedtuple("Users", "id name, password")
        with BDConnectionHandler() as connection:
            try:
                newUser = Users(name=name, password=password)
                connection.session.add(newUser)
                connection.session.commit()

                return insertData(newUser.id, newUser.name, newUser.password)
            except:
                connection.session.rollback()
                raise
            finally:
                connection.session.close()
        return None
