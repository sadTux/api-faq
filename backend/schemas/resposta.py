from pydantic import BaseModel

class Resposta(BaseModel):

  resposta: str
  nome_usuario: str
  pergunta: str