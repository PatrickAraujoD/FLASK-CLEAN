from src.domain.models import Users
from src.infra.config import BDConnectionHandler
from src.infra.entities import Users as UsersModel


class UserRepository:
    @classmethod
    def insertUser(cls, name: str, password: str) -> Users:
        with BDConnectionHandler() as connection:
            try:
                newUser = UsersModel(name=name, password=password)
                connection.session.add(newUser)
                connection.session.commit()

                return Users(newUser.id, newUser.name, newUser.password)
            except:
                connection.session.rollback()
                raise
            finally:
                connection.session.close()
        return None
