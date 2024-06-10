from faker import Faker
from src.infra.test import UsersRepositorySpy
from .find_user_use_case import FindUserUseCase

faker = Faker()


def testFindById():
    """Testing by_id method in FindUser"""

    userRepo = UsersRepositorySpy()
    findUser = FindUserUseCase(userRepo)

    attribute = {"id": faker.random_number(digits=2)}
    response = findUser.findById(user_id=attribute["id"])

    # Testing Input
    assert userRepo.selectUserParams["userId"] == attribute["id"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def testFailFindById():
    """Testing by_id fail method in FindUser"""

    userRepo = UsersRepositorySpy()
    findUser = FindUserUseCase(userRepo)

    attribute = {"id": faker.word()}
    response = findUser.findById(user_id=attribute["id"])

    # Testing Input
    assert userRepo.selectUserParams == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None


def testFindByName():
    """Testing by_name method in FindUser"""

    userRepo = UsersRepositorySpy()
    findUser = FindUserUseCase(userRepo)

    attribute = {"name": faker.word()}
    response = findUser.findByName(name=attribute["name"])

    # Testing Input
    assert userRepo.selectUserParams["name"] == attribute["name"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def testFailFindByName():
    """Testing by_name fail method in FindUser"""

    userRepo = UsersRepositorySpy()
    findUser = FindUserUseCase(userRepo)

    attribute = {"name": faker.random_number(digits=2)}
    response = findUser.findByName(name=attribute["name"])

    # Testing Input
    assert userRepo.selectUserParams == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None


def testFindByIdAndName():
    """Testing by_id_and_name method in FindUser"""

    userRepo = UsersRepositorySpy()
    findUser = FindUserUseCase(userRepo)

    attribute = {"user_id": faker.random_number(digits=2), "name": faker.word()}

    response = findUser.findByIdAndName(
        user_id=attribute["user_id"], name=attribute["name"]
    )

    # Testing Input
    assert userRepo.selectUserParams["userId"] == attribute["user_id"]
    assert userRepo.selectUserParams["name"] == attribute["name"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def testFailFindByIdAndName():
    """Testing by_id_and_name fail method in FindUser"""

    userRepo = UsersRepositorySpy()
    findUser = FindUserUseCase(userRepo)

    attribute = {
        "user_id": faker.random_number(digits=2),
        "name": faker.random_number(digits=2),
    }

    response = findUser.findByIdAndName(
        user_id=attribute["user_id"], name=attribute["name"]
    )

    # Testing Input
    assert userRepo.selectUserParams == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] is None
