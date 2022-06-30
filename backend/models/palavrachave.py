from sqlalchemy import Column, ForeignKey, Integer, String, Text
from backend.db.base_class import Base

class Palavrachave(Base):
    __tablename__ = "palavrachave"
    id = Column(Integer, primary_key = True)
    palavrachave = Column(String, unique = True, nullable = False)