from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models import Users


class RegisterUserInterface(ABC):
    @abstractmethod
    def execute(cls, name: str, password: str) -> Dict[bool, Users]:
        raise Exception("Should implement method: Execute")
