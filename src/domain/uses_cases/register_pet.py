from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models import Pets


class RegisterPets(ABC):
    @abstractmethod
    def execute(
        cls, name: str, specie: str, userInfo: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        raise Exception("Should implement method")
