from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.infra.config import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    idPet = relationship("Pets")

    def __rep__(self):
        return f"User [name={self.name}]"

    def __eq__(self, other):
        if isinstance(other, Users):
            return (
                self.id == other.id
                and self.name == other.name
                and self.password == other.password
            )
        return False
