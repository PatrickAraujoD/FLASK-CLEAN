from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Pets


class FindPetInterface(ABC):
    """Interface to FindPet use case"""

    @abstractmethod
    def findByPetId(cls, user_id: int) -> Dict[bool, List[Pets]]:
        """Specific Case"""

        raise Exception("Should implement method: by_id")

    @abstractmethod
    def findByUserId(cls, name: str) -> Dict[bool, List[Pets]]:
        """Specific Case"""

        raise Exception("Should implement method: by_name")

    @abstractmethod
    def findByPetIdAndUserId(cls, user_id: int, userId: int) -> Dict[bool, List[Pets]]:
        """Specific Case"""

        raise Exception("Should implement method: by_name")
