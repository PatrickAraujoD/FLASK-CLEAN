from faker import Faker
from src.infra.test import PetRepositorySpy
from .find_pet_use_case import FindPetUseCase

faker = Faker()


def testFindByPetId():
    petRepo = PetRepositorySpy()
    findPet = FindPetUseCase(petRepo)

    attribute = {"id": faker.random_number(digits=2)}
    response = findPet.findByPetId(petId=attribute["id"])

    # Testing Input
    assert petRepo.selectPetParams["petId"] == attribute["id"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]


def testFailFindByPetId():
    """Testing by_id method in FindPet"""

    petRepo = PetRepositorySpy()
    findPet = FindPetUseCase(petRepo)

    attribute = {"id": faker.name()}
    response = findPet.findByPetId(petId=attribute["id"])

    # Testing Input
    assert petRepo.selectPetParams == {}

    # Testing Outputs
    assert response["Success"] is False
    assert response["Data"] == None


def testFindByPetUserId():
    petRepo = PetRepositorySpy()
    findPet = FindPetUseCase(petRepo)

    attribute = {"userId": faker.random_number()}

    response = findPet.findByUserId(userId=attribute["userId"])

    assert petRepo.selectPetParams["userId"] == attribute["userId"]
    assert response["Success"] is True
    assert response["Data"]


def testFindFailByPetUserId():
    petRepo = PetRepositorySpy()
    findPet = FindPetUseCase(petRepo)

    attribute = {"userId": faker.name()}

    response = findPet.findByUserId(userId=attribute["userId"])

    assert response["Success"] is False
    assert response["Data"] == None


def testFindByPetUserIdAndPetId():
    petRepo = PetRepositorySpy()
    findPet = FindPetUseCase(petRepo)

    attribute = {"userId": faker.random_number(), "petId": faker.random_number()}

    response = findPet.findByPetIdAndUserId(
        userId=attribute["userId"], petId=attribute["petId"]
    )

    assert petRepo.selectPetParams["userId"] == attribute["userId"]
    assert petRepo.selectPetParams["petId"] == attribute["petId"]
    assert response["Success"] is True
    assert response["Data"]


def testFailFindByPetUserIdAndPetId():
    petRepo = PetRepositorySpy()
    findPet = FindPetUseCase(petRepo)

    attribute = {"userId": faker.name(), "petId": faker.random_number()}

    response = findPet.findByPetIdAndUserId(
        userId=attribute["userId"], petId=attribute["petId"]
    )

    assert response["Success"] is False
    assert response["Data"] == None
