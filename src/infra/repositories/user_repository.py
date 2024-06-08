from typing import List
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

    @classmethod
    def selectUser(cls, userId: int = None, name: str = None) -> List[Users]:
        try:
            query_data = None
            with BDConnectionHandler() as connection:
                if userId and not name:
                    data = (
                        connection.session.query(UsersModel).filter_by(id=userId).one()
                    )
                    query_data = [data]

                elif name and not userId:
                    data = (
                        connection.session.query(UsersModel).filter_by(name=name).one()
                    )
                    query_data = [data]

                elif userId and name:
                    data = (
                        connection.session.query(UsersModel)
                        .filter_by(id=userId, name=name)
                        .one()
                    )
                    query_data = [data]

                return query_data
        except:
            connection.session.close()
            raise
        finally:
            connection.session.close()
