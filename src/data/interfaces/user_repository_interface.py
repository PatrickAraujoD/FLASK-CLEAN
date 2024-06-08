from typing import List
from abc import ABC, abstractmethod
from src.domain.models import Users


class UsersRepositoryInterface(ABC):
    @abstractmethod
    def insertUser(cls, name: str, password: str) -> Users:
        raise Exception("Method not Implemented")

    @abstractmethod
    def selectUser(cls, userId: int = None, name: str = None) -> List[Users]:
        raise Exception("Method not Implemented")
