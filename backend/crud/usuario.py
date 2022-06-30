from sqlalchemy.orm import Session
from backend.schemas.usuario import criaUsuario
from backend.models.usuario import Usuario

def criaUsuario(db:Session, usuario: criaUsuario):
    db_usuario = Usuario(email = usuario.email, nome = usuario.nome, apelido = usuario.apelido, senha = usuario.senha)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)

    return db_usuario