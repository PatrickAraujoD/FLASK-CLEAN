from typing import Dict, Type, List
from src.data.find_user import FindUserUseCase
from src.domain.models import Pets, Users
from src.domain.uses_cases import RegisterPets as RegisterPetsInterface
from src.data.interfaces import PetRepositoryInterface


class RegisterPetUseCase(RegisterPetsInterface):
    def __init__(
        self,
        petRepository: Type[PetRepositoryInterface],
        findUserUseCase: type[FindUserUseCase],
    ):
        self.petRepository = petRepository
        self.findUserUseCase = findUserUseCase

    def execute(
        cls, name: str, specie: str, userInfo: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        response = None
        validateEntry = isinstance(name, str) and isinstance(specie, str)

    def __find_user_information(
        self, userInfo: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        userFounded = None
        userParams = userInfo.keys()

        if "userId" in userParams and "name" in userParams:
            userFounded = self.findUserUseCase.findByIdAndName(
                user_id=userInfo["userId"], name=userInfo["name"]
            )
        elif "userId":
            userFounded = self.findUserUseCase.findById(user_id=userInfo["userId"])
        elif "name":
            userFounded = self.findUserUseCase.findByName(name=userInfo["name"])
