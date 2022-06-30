from sqlalchemy import Column, Integer, String
from backend.db.base_class import Base

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key = True)
    email = Column(String, nullable = False, unique = True, index = True)
    senha = Column(String, nullable = False)
    nome = Column(String, nullable = False)
    apelido = Column(String, nullable = False, index = True, unique = True)