from typing import List
from src.domain.models import Pets
from src.data.interfaces import PetRepositoryInterface
from src.domain.test import petsMock

class PetRepositorySpy(PetRepositoryInterface):
    def __init__(self):
        self.insertPetParams = {}
        self.selectPetParams = {}

    def insertPet(self, name: str, specie: str, age: int, userId: int, petId: int) -> Pets:
        self.insertPetParams["petId"] = petId
        self.insertPetParams["name"] = name
        self.insertPetParams["specie"] = specie
        self.insertPetParams["age"] = age
        self.insertPetParams["userId"] = userId

        return petsMock()

    def selectPet(self, petId: int = None, userId: int = None) -> List[Pets]:
        self.selectPetParams["petId"] = petId
        self.selectPetParams["userId"] = userId

        print(self.selectPetParams)

        return [petsMock()]
