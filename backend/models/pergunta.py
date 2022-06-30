from sqlalchemy import Column, ForeignKey, Integer, String, Text
from backend.db.base_class import Base

class Pergunta(Base):
    __tablename__ = "pergunta"
    id = Column(Integer, primary_key = True)
    titulo = Column(String, nullable = False)
    texto = Column(Text, nullable = False)
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable = False)