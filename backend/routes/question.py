from fastapi import APIRouter

apiRouter = APIRouter()

@apiRouter.post("/")
def createQuestion():
  return {"msg": "Created"}

@apiRouter.get("/")
def getAllQuestions():
  return [{"question": "ask"}]

@apiRouter.get("/{id}")
def getQuestion(id:int):
  return {"question": "ask"}

@apiRouter.delete("/{id}")
def removeQuestion(id:int):
  return {"msg": "Deleted"}