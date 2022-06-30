from pydantic import BaseModel

class criaUsuario(BaseModel):
  email: str
  nome: str
  apelido:str
  senha: str
