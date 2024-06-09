import pytest
from faker import Faker
from .register_user_use_case import RegisterUserUseCase
from src.infra.test import UsersRepositorySpy

faker = Faker()


def testRegisterUserUseValidData():
    usersRepository = UsersRepositorySpy()
    registerUser = RegisterUserUseCase(usersRepository)

    attributes = {"name": faker.name(), "password": faker.name()}

    response = registerUser.execute(attributes["name"], attributes["password"])

    assert usersRepository.insertUserParams["name"] == attributes["name"]
    assert usersRepository.insertUserParams["password"] == attributes["password"]

    assert response["Sucess"] is True
    assert response["Data"]


def testRegisterUserUseCaseInValidData():
    usersRepositorySpy = UsersRepositorySpy()
    registerUserUseCase = RegisterUserUseCase(usersRepositorySpy)

    with pytest.raises(Exception) as excInfo:
        registerUserUseCase.execute(name=123, password="dksjdkjskdjsk")

    assert str(excInfo.value) == "Data not is valid"
