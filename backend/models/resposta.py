from sqlalchemy import Column, ForeignKey, Integer, String, Text
from backend.db.base_class import Base

class Resposta(Base):
    __tablename__ = "resposta"
    id = Column(Integer, primary_key = True)
    texto = Column(Text, nullable = False)
    pergunta_id = Column(Integer, ForeignKey("pergunta.id"), nullable = False)
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable = False)