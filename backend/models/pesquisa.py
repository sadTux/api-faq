from sqlalchemy import Column, ForeignKey, Integer, String, Text
from backend.db.base_class import Base

class Pesquisa(Base):
    __tablename__ = "pesquisa"
    palavrachave_id = Column(Integer, ForeignKey("palavrachave.id"), primary_key = True, nullable = False)
    pergunta_id = Column(Integer, ForeignKey("pergunta.id"), primary_key = True, nullable = False)