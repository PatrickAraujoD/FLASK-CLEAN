import enum
from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from src.infra.config import Base


class AnimalType(enum.Enum):
    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"


class Pets(Base):
    __tablename__ = "pets"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    specie = Column(Enum(AnimalType), nullable=False)
    age = Column(Integer, nullable=True)
    userId = Column(Integer, ForeignKey("users.id"))

    def __rep__(self):
        return (
            f"Pet: [pet = {self.pet}, specie = {self.specie} and userId: {self.userId}]"
        )
