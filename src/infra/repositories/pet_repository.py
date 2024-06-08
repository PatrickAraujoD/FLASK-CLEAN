from typing import List
from src.domain.models import Pets
from src.data.interfaces import PetRepositoryInterface
from src.infra.entities import Pets as PetsModel
from src.infra.config import BDConnectionHandler


class PetRepository(PetRepositoryInterface):
    @classmethod
    def insertPet(cls, name: str, specie: str, age: int, userId: int) -> Pets:
        with BDConnectionHandler() as connection:
            try:
                newPet = PetsModel(name=name, specie=specie, age=age, userId=userId)
                connection.session.add(newPet)
                connection.session.commit()

                return Pets(
                    newPet.id, newPet.name, newPet.specie, newPet.age, newPet.userId
                )
            except:
                connection.session.rollback()
                raise
            finally:
                connection.session.close()

    @classmethod
    def selectPet(cls, petId: int = None, userId: int = None) -> List[Pets]:
        with BDConnectionHandler() as connection:
            query_data = None
            try:
                if petId and not userId:
                    data = connection.session.query(PetsModel).filter_by(id=petId).one()
                    query_data = [data]
                elif not petId and userId:
                    data = (
                        connection.session.query(PetsModel)
                        .filter_by(userId=userId)
                        .all()
                    )
                    query_data = data
                elif petId and userId:
                    data = (
                        connection.session.query(PetsModel)
                        .filter_by(id=petId, userId=userId)
                        .one()
                    )
                    query_data = [data]

                return query_data
            except:
                connection.session.rollback()
                raise
            finally:
                connection.session.close()
