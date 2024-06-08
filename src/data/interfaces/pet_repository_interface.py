from typing import List
from abc import ABC, abstractmethod
from src.domain.models import Pets


class PetRepositoryInterface(ABC):
    @abstractmethod
    def insertPet(self, specie: str, age: int, userId: int, name: str) -> Pets:
        raise Exception("Method not Implemented")

    @abstractmethod
    def selectPet(self, petId: int = None, userId: int = None) -> List[Pets]:
        raise Exception("Method not Implemented")
