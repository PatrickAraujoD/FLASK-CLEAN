from typing import Dict, Type
from src.domain.models import Users
from src.domain.uses_cases import RegisterUserInterface
from src.data.interfaces import UsersRepositoryInterface


class RegisterUserUseCase(RegisterUserInterface):
    def __init__(self, UsersRepositoty: Type[UsersRepositoryInterface]):
        self.userRepository = UsersRepositoty

    def execute(self, name: str, password: str) -> Dict[bool, Users]:
        validateEntry = isinstance(name, str) and isinstance(password, str)

        if not validateEntry:
            raise Exception("Data not is valid")

        response = self.userRepository.insertUser(name=name, password=password)

        return {"Sucess": validateEntry, "Data": response}
