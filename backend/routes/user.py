from fastapi import APIRouter, Depends
from backend.schemas.usuario import criaUsuario as Usuario
from backend.crud.usuario import criaUsuario
from backend.db.sessao import obtem_DB
from sqlalchemy.orm import Session

apiRouter = APIRouter()

@apiRouter.post("/")
def createUser(usuario: Usuario, db: Session = Depends(obtem_DB)):
  criaUsuario(db=db, usuario=usuario)
  return {"msg": "Created"}

@apiRouter.delete("/{id}")
def removeUser(id:int):
  return {"msg": "Deleted"}