from faker import Faker
from sqlalchemy import text
from .pet_repository import PetRepository
from src.infra.config import BDConnectionHandler
from src.infra.entities.pets import Pets, AnimalType

faker = Faker()
petRepository = PetRepository()
connection = BDConnectionHandler()


def testInsertPet():
    """Should Insert Pet table and return it"""
    name = faker.name()
    specie = "fish"
    age = faker.random_number(digits=1)
    userId = faker.random_number()

    newPet = petRepository.insertPet(name, specie, age, userId)

    engine = connection.getEngine()

    with engine.connect() as conn:
        query = text("SELECT * FROM pets WHERE id=:idPet")
        pet = conn.execute(query, {"idPet": newPet.id}).fetchone()

        query = text("DELETE FROM pets WHERE id=:idPet")
        conn.execute(query, {"idPet": newPet.id})
        conn.commit()

    assert pet is not None
    assert pet.id == newPet.id
    assert pet.name == newPet.name
    assert pet.age == newPet.age
    assert pet.specie == newPet.specie.value
    assert pet.userId == newPet.userId


def testSelectPet():
    """Should select a pet in Users table and compare it"""
    petId = faker.random_number(digits=5)
    name = faker.name()
    specieMok = AnimalType("cat")
    userId = 2
    age = faker.random_number(digits=1)
    data = Pets(id=petId, name=name, specie=specieMok, userId=userId, age=age)

    engine = connection.getEngine()

    with engine.connect() as conn:
        query = text(
            "INSERT INTO pets(id, name, specie, userId, age) VALUES (:petId, :name, :specie, :userId, :age)"
        )
        conn.execute(
            query,
            {
                "petId": petId,
                "name": name,
                "age": age,
                "userId": userId,
                "specie": specieMok.value,
            },
        )
        conn.commit()

    resultPet = petRepository.selectPet(petId=petId)
    resultPet1 = petRepository.selectPet(userId=userId)
    resultPet2 = petRepository.selectPet(petId=petId, userId=userId)

    print(resultPet1)
    assert data in resultPet
    assert data in resultPet1
    assert data in resultPet2

    # with engine.connect() as conn:
    #     query = text("DELETE FROM pets WHERE id=:id")
    #     conn.execute(query, {"id": petId})
    #     conn.commit()
