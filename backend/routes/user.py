from fastapi import APIRouter

apiRouter = APIRouter()

@apiRouter.post("/")
def createUser():
  return {"msg": "Created"}

@apiRouter.delete("/{id}")
def removeUser(id:int):
  return {"msg": "Deleted"}