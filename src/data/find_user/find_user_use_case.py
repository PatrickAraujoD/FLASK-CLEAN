from typing import Type, Dict, List
from src.domain.uses_cases import FindUserInterface
from src.data.interfaces import UsersRepositoryInterface as UserRepository
from src.domain.models import Users


class FindUserUseCase(FindUserInterface):
    """Class to define use case Find User"""

    def __init__(self, userRepository: Type[UserRepository]):
        self.userRepository = userRepository

    def findById(self, user_id: int) -> Dict[bool, List[Users]]:
        """Select User By id
        :param - user_id: id of the user
        :param - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.userRepository.selectUser(userId=user_id)

        return {"Success": validate_entry, "Data": response}

    def findByName(self, name: str) -> Dict[bool, List[Users]]:
        """Select User By name
        :param - name: name of the user
        :param - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.userRepository.selectUser(name=name)

        return {"Success": validate_entry, "Data": response}

    def findByIdAndName(self, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """Select User By id and name
        :param - user_id: id of the user
               - name: name of the user
        :param - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(name, str) and isinstance(user_id, int)

        if validate_entry:
            response = self.userRepository.selectUser(userId=user_id, name=name)

        return {"Success": validate_entry, "Data": response}
