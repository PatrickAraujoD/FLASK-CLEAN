from typing import List
from src.data.interfaces import UsersRepositoryInterface
from src.domain.models import Users
from src.domain.test import mockUser


class UsersRepositorySpy(UsersRepositoryInterface):
    def __init__(self):
        self.insertUserParams = {}
        self.selectUserParams = {}

    def insertUser(self, name: str, password: str):
        self.insertUserParams["name"] = name
        self.insertUserParams["password"] = password

        return mockUser()

    def selectUser(self, userId: int = None, name: str = None) -> List[Users]:
        self.selectUser["userId"] = userId
        self.selectUser["name"] = name

        return [mockUser()]
