from faker import Faker
from src.domain.models import Users

faker = Faker()


def mockUser():
    id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.name()

    return Users(id, name, password)
