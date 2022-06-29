from fastapi import APIRouter

apiRouter = APIRouter()

@apiRouter.get("/generate-token-login")
def generateTokenLogin():
  return {"token": "jvhad4euf*hy89"}
