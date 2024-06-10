from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Users


class FindUserInterface(ABC):
    """Interface to FindPet use case"""

    @abstractmethod
    def findById(cls, user_id: int) -> Dict[bool, List[Users]]:
        """Specific Case"""

        raise Exception("Should implement method: by_id")

    @abstractmethod
    def findByName(cls, name: str) -> Dict[bool, List[Users]]:
        """Specific Case"""

        raise Exception("Should implement method: by_name")

    @abstractmethod
    def findByIdAndName(cls, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """Specific Case"""

        raise Exception("Should implement method: by_name")
