from faker import Faker
from src.domain.models import Pets


def petsMock():
    faker = Faker()
    id = faker.random_number(digits=5)
    name = faker.name()
    specie = "fish"
    age = faker.random_number(digits=1)
    userId = faker.random_number(digits=5)

    Pets(id, name, specie, age, userId)
