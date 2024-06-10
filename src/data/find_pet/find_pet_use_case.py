from typing import Type, Dict, List
from src.domain.uses_cases import FindPetInterface
from src.data.interfaces import PetRepositoryInterface
from src.domain.models import Pets

class FindPetUseCase(FindPetInterface):
    """Class to define use case Find User"""

    def __init__(self, petRepository: Type[PetRepositoryInterface]):
        self.petRepository = petRepository

    def findByPetId(self, petId: int) -> Dict[bool, List[Pets]]:
        response = None
        validate_entry = isinstance(petId, int)

        if validate_entry:
            response = self.petRepository.selectPet(petId=petId)

        return {"Success": validate_entry, "Data": response}

    def findByUserId(self, userId: int) -> Dict[bool, List[Pets]]:
        response = None
        validate_entry = isinstance(userId, int)

        if validate_entry:
            response = self.petRepository.selectPet(userId=userId)

        return {"Success": validate_entry, "Data": response}

    def findByPetIdAndUserId(self, petId: int, userId: int) -> Dict[bool, List[Pets]]:

        response = None
        validate_entry = isinstance(userId, int) and isinstance(petId, int)

        if validate_entry:
            response = self.petRepository.selectPet(petId=petId, userId=userId)

        return {"Success": validate_entry, "Data": response}
