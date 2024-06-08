from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from src.infra.config import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    idPet = relationship("Pets")

    def __rep__(self):
        return f"User [name={self.name}]"
